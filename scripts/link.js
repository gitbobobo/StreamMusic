const fs = require("fs");
const crypto = require("crypto");
const yargs = require("yargs/yargs");
const { hideBin } = require("yargs/helpers");

const argv = yargs(hideBin(process.argv)).argv;

const version = argv._[0];
const dirPath = argv._[1];

console.log(`Version: ${version}`);
console.log(`Directory: ${dirPath}`);

var androidArm64Md5 = "Unknown";
var androidArmv7Md5 = "Unknown";
var androidX86Md5 = "Unknown";
var androidUniversalMd5 = "Unknown";
var windowsMd5 = "Unknown";
var macMd5 = "Unknown";

// 读取目录下所有文件，输出 md5 值
fs.readdir(dirPath, (err, files) => {
  if (err) {
    console.error(err);
    return;
  }
  files.forEach((file) => {
    const filePath = `${dirPath}/${file}`;
    const stats = fs.statSync(filePath);
    if (stats.isDirectory()) {
      console.log(`${file} is a directory`);
    } else {
      const content = fs.readFileSync(filePath);
      const md5 = crypto.createHash("md5").update(content).digest("hex");
      console.log(`${file}: ${md5}`);
      if (file === "app-arm64-v8a-release.apk") {
        androidArm64Md5 = md5;
      } else if (file === "app-armeabi-v7a-release.apk") {
        androidArmv7Md5 = md5;
      } else if (file === "app-x86_64-release.apk") {
        androidX86Md5 = md5;
      } else if (file === "app-release.apk") {
        androidUniversalMd5 = md5;
      } else if (file.endsWith(".dmg")) {
        macMd5 = md5;
      } else if (file.endsWith(".msix")) {
        windowsMd5 = md5;
      }
    }
  });

  const template = `
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Button from '@mui/material/Button';
import WindowIcon from '@mui/icons-material/Window';
import AppleIcon from '@mui/icons-material/Apple';
import AndroidIcon from '@mui/icons-material/Android';

<Tabs groupId="operating-systems">
<TabItem value="android" label="Android">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} target="_blank" href="https://oss2.aqzscn.cn/stream-music/versions/${version}/app-arm64-v8a-release.apk">ARM64 版本</Button>
    <span class="ml-md gray">MD5: ${androidArm64Md5}</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} target="_blank" href="https://oss2.aqzscn.cn/stream-music/versions/${version}/app-armeabi-v7a-release.apk">ARMV7 版本</Button>
    <span class="ml-md gray">MD5: ${androidArmv7Md5}</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} target="_blank" href="https://oss2.aqzscn.cn/stream-music/versions/${version}/app-x86_64-release.apk">x86 版本</Button>
    <span class="ml-md gray">MD5: ${androidX86Md5}</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} target="_blank" href="https://oss2.aqzscn.cn/stream-music/versions/${version}/app-release.apk">通用版本（体积较大）</Button>
    <span class="ml-md gray">MD5: ${androidUniversalMd5}</span>
</div>
</TabItem>

<TabItem value="win" label="Windows">
<div class="mv-sm">
    <Button variant="contained" startIcon={<WindowIcon />} target="_blank" href="https://oss2.aqzscn.cn/stream-music/versions/${version}/stream_music_${version}.0.msix">立即下载</Button>
    <span class="ml-md gray">MD5: ${windowsMd5}</span>
</div>

:::caution

若安装失败请查看[安装教程](../guides/install)

:::
</TabItem>

<TabItem value="mac" label="macOS">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AppleIcon />} target="_blank" href="https://oss2.aqzscn.cn/stream-music/versions/${version}/StreamMusic_${version}.dmg">立即下载</Button>
    <span class="ml-md gray">MD5: ${macMd5}</span>
</div>
</TabItem>
</Tabs>
`;

  console.log(template);
});
