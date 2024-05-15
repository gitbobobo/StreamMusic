// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: '音流',
  tagline: '连接你的音乐',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://music.aqzscn.cn/',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'gitbobobo', // Usually your GitHub org/user name.
  projectName: 'StreamMusic', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'zh-Hans',
    locales: ['zh-Hans'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/gitbobobo/StreamMusic/blob/main/',
            async sidebarItemsGenerator({defaultSidebarItemsGenerator, ...args}) {
              const sidebarItems = await defaultSidebarItemsGenerator(args);
              return reverseSidebarItems(sidebarItems);
            },
          },
        // blog: {
        //   showReadingTime: true,
        //   // Please change this to your repo.
        //   // Remove this to remove the "edit this page" links.
        //   editUrl:
        //     'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        // },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: '音流',
        logo: {
          alt: 'Stream Music\'s Logo',
          src: 'img/logo.png',
        },
        items: [
          // {
          //   type: 'docSidebar',
          //   sidebarId: 'tutorialSidebar',
          //   position: 'left',
          //   label: '文档',
          // },
          // {to: '/blog', label: '博客', position: 'left'},
          {
            type: 'html',
            position: 'right',
            value: '<a class="navbar__item navbar__link header-github-link" rel="noopener noreferrer" target="_blank" aria-label="GitHub repository" href="https://github.com/gitbobobo/StreamMusic"></a>',
          },
        ],
      },
      // footer: {
      //   style: 'dark',
      //   copyright: `Copyright © ${new Date().getFullYear()} 音流, Inc. 由 Docusaurus 构建.`,
      // },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['json', 'php', 'dart'],
      },
    }),
};

function reverseSidebarItems(items, reverse = false) {
  // Reverse items in categories
  const result = items.map((item) => {
    if (item.type === 'category') {
      // console.log(item)
      const r = item.customProps && item.customProps.reversed
      return {...item, items: reverseSidebarItems(item.items, r)};
    }
    // console.log(item)
    return item;
  });
  // console.log(items)
  // Reverse items at current level
  if (reverse) {
    result.reverse();
  }
  return result;
}

export default config;
