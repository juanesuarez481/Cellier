import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import { Inter } from '@next/font/google'
import styles from '@/styles/Quantities.module.css'
const inter = Inter({ subsets: ['latin'] })

export default function Ingredients({ data2 }) {
  return (
    <>
      <Head>
        <title>Cellier</title>
        <meta name="description" content="Cellier food assistant" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>

        <div className={styles.description}>
          <Link href="/">
            <h1>
              Cellier
            </h1>
          </Link>
          <div>
            <Image
              src="/cellier-logo-square.png"
              alt="cellier-logo-square"
              className={styles.vercelLogo}
              width={512}
              height={512}
              priority
            />
          </div>
        </div>

        <div className={styles.center}>

          <div className={styles.images}>
            <h2 className={inter.className}>
              Quantities
            </h2>
            <Image
              className={styles.logo}
              src="/quantities-home.png"
              alt="quantities-home"
              width={512}
              height={512}
              priority
            />
          </div>
        </div>

        <div className={styles.grid}>
          {data2.map(
            (element) =>
              <div
                key={element.id}
                className={styles.card}
              >
                <h2 className={inter.className}>
                  {element.value + ' ' + element.unit.name}
                </h2>
                <div className={styles.icono}>
                  <Image
                    src={"/unit-" + element.unit.related_name + ".png"}
                    alt={"unit-" + element.unit.related_name}
                    className={styles.iconocomida}
                    width={80}
                    height={80}
                    priority
                  />
                  <Image
                    src={"/ingredient-" + element.ingredient.related_name + ".png"}
                    alt={"ingredient-" + element.ingredient.related_name}
                    className={styles.iconocomida}
                    width={80}
                    height={80}
                    priority
                  />
                </div>
                <p className={inter.className}>
                  {'( ' + element.ingredient.related_name + ' )'}
                </p>
              </div>
          )}
        </div>

      </main>
    </>
  )
}

export async function getStaticProps() {
  const base64 = require('base-64');
  const response2 = await fetch("http://192.168.1.7:8000/api/quantities/")
  const data2 = await response2.json()
  return {
    props: {
      data2: data2,
    }
  }
}
