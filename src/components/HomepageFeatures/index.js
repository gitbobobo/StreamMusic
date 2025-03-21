import clsx from "clsx";
import Heading from "@theme/Heading";
import Translate, { translate } from "@docusaurus/Translate";
import styles from "./styles.module.css";

const FeatureList = [
  {
    title: translate({ message: "Easy to Use" }),
    Svg: require("@site/static/img/undraw_docusaurus_tree.svg").default,
    description: (
      <Translate>
        Carefully designed interface allows you to get started quickly
      </Translate>
    ),
  },
  {
    title: translate({ message: "Focus on Music" }),
    Svg: require("@site/static/img/undraw_docusaurus_mountain.svg").default,
    description: (
      <Translate>
        Supports common music services, allowing you to access multiple music
        services through one client
      </Translate>
    ),
  },
  {
    title: translate({ message: "Cross-Platform Support" }),
    Svg: require("@site/static/img/undraw_docusaurus_react.svg").default,
    description: (
      <Translate>
        Available on Android, iOS, macOS, and Windows, providing a consistent
        experience across platforms
      </Translate>
    ),
  },
];

function Feature({ Svg, title, description }) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
