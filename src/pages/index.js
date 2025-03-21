import clsx from "clsx";
import Link from "@docusaurus/Link";
import Layout from "@theme/Layout";
import HomepageFeatures from "@site/src/components/HomepageFeatures";
import Button from "@mui/material/Button";
import DownloadIcon from "@mui/icons-material/Download";
import ArrowForwardIcon from "@mui/icons-material/ArrowForward";
import Translate from "@docusaurus/Translate";

import Heading from "@theme/Heading";
import styles from "./index.module.css";

function HomepageHeader() {
  return (
    <header className={clsx("hero hero--primary", styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          <Translate>StreamMusic</Translate>
        </Heading>
        <p className="hero__subtitle">
          <Translate>Enjoy your Music</Translate>
        </p>
        <div className={styles.buttons}>
          <Link to="/docs/versions/latest" className={styles.buttonWrapper}>
            <Button
              variant="contained"
              startIcon={<DownloadIcon />}
              size="large">
              <Translate>Download</Translate>
            </Button>
          </Link>
          <Link to="/docs/intro" className={styles.buttonWrapper}>
            <Button
              variant="contained"
              endIcon={<ArrowForwardIcon />}
              size="large">
              <Translate>QuickStart</Translate>
            </Button>
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  return (
    <Layout description="音流是一款跨平台的 NAS 音乐播放器。">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
