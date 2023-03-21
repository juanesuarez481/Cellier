import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import { Inter } from '@next/font/google'
import styles from '@/styles/Recipes.module.css'
const inter = Inter({ subsets: ['latin'] })

export async function getStaticProps() {
  // const base64 = require('base-64');
  // const response1 = await fetch("http://192.168.1.7:8000/api/recipes/", {
  //   headers: new Headers({
  //     "Authorization": `Basic ${base64.encode(`${"AnonymousTest"}:${"Cellier_test*"}`)}`
  //   }),
  // })
  const response = await fetch("http://192.168.1.7:8000/api/recipes/")
  const data = await response.json()
  return {
    props: {
      data: data,
    }
  }
}

export default function Recipes({ data }) {
  return (
    <>
      <Head>
        <title>Cellier</title>
        <meta name="description" content="Cellier food assistant" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>

        <div className={styles.center}>
          <div className={styles.images}>
            <h2 className={inter.className}>
              Recipes
            </h2>
            <Image
              className={styles.logo}
              src="/recipes-home.png"
              alt="recipes-home"
              width={512}
              height={512}
              priority
            />
          </div>
        </div>

        <div className={styles.grid}>
          {data.map(
            (element) =>
              <div
                key={element.id}
                className={styles.card}
              >
                <h2 className={inter.className}>
                  {element.name}
                </h2>
                <div className={styles.icono}>
                  <Image
                    src={"/recipe-" + element.related_name + ".png"}
                    alt={"recipe-" + element.related_name}
                    className={styles.iconocomida}
                    width={80}
                    height={80}
                    priority
                  />
                </div>
                <h4 className={inter.className}>
                  Ingredients {
                    element.quantities.length <= 4
                      ? '[' + element.quantities.length + ']'
                      : '[+' + element.quantities.length + ']'
                  }
                </h4>
                {element.quantities.slice(0, 4).map(
                  (quantity) =>
                    <div key={quantity.id}>
                      <p className={inter.className}>
                        {quantity.value + ' ' + quantity.unit.name + ' de ' + quantity.ingredient.name}
                      </p>

                    </div>
                )}
                <h4 className={inter.className}>
                  Difficulty / Preparation time
                </h4>
                <h3 className={inter.className}>
                  {element.difficulty + " / "
                    + element.preparation_time}
                </h3>
              </div>
          )}
        </div>
      </main>
    </>
  )
}
