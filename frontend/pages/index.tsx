import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Head>
        <title>Cellier</title>
        <meta name="description" content="Cellier food assistant" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>

        <div className={styles.contcenter}>
          <div className={styles.centerimg}>
            <div className={styles.imgtxt}>
              <h2 className={inter.className}>
                Encuentra las recetas, alimentos
                e historias que mas te gustan aqui
              </h2>
              <Image
                className={styles.imgbackground}
                src="/home-bg1.png"
                alt="home-bg1"
                width={512}
                height={512}
                priority
              />
            </div>
            <div className={styles.imgtxt}>
              <h2 className={inter.className}>
                Guarda y agrupa tus
                preferencias en cantidades, nutrición,
                ingredientes y mas
              </h2>
              <Image
                className={styles.imgbackground}
                src="/home-bg3.png"
                alt="home-bg3"
                width={512}
                height={512}
                priority
              />
            </div>
            <div className={styles.imgtxt}>
              <h2 className={inter.className}>
                Disfruta de información sobre tus
                ingredientes y sus cualidades
                nutricionales
              </h2>
              <Image
                className={styles.imgbackground}
                src="/home-bg2.png"
                alt="home-bg2"
                width={512}
                height={512}
                priority
              />
            </div>
          </div>

          <div className={styles.center}>
            <Link href="/">
              <div className={styles.images}>
                <h2 className={inter.className}>
                  Pantries
                </h2>
                <Image
                  className={styles.logo}
                  src="/pantries-home.png"
                  alt="pantries-home"
                  width={512}
                  height={512}
                  priority
                />
              </div>
            </Link>

            <Link href="/recipes">
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
            </Link>

            <Link href="/ingredients">
              <div className={styles.images}>
                <h2 className={inter.className}>
                  Ingredients
                </h2>
                <Image
                  className={styles.logo}
                  src="/ingredients-home.png"
                  alt="ingredients-home"
                  width={512}
                  height={512}
                  priority
                />
              </div>
            </Link>

            <Link href="/quantities">
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
            </Link>
            <Link href="/units">
              <div className={styles.images}>
                <h2 className={inter.className}>
                  Units
                </h2>
                <Image
                  className={styles.logo}
                  src="/units-home.png"
                  alt="units-home"
                  width={512}
                  height={512}
                  priority
                />
              </div>
            </Link>
            <Link href="/">
              <div className={styles.images}>
                <h2 className={inter.className}>
                  Nutrition
                </h2>
                <Image
                  className={styles.logo}
                  src="/nutrition-home.png"
                  alt="nutrition-home"
                  width={512}
                  height={512}
                  priority
                />
              </div>
            </Link>
            <Link href="/">
              <div className={styles.images}>
                <h2 className={inter.className}>
                  Information
                </h2>
                <Image
                  className={styles.logo}
                  src="/info-home.png"
                  alt="info-home"
                  width={512}
                  height={512}
                  priority
                />
              </div>
            </Link>
            <Link href="/">
              <div className={styles.images}>
                <h2 className={inter.className}>
                  Facts
                </h2>
                <Image
                  className={styles.logo}
                  src="/facts-home.png"
                  alt="facts-home"
                  width={512}
                  height={512}
                  priority
                />
              </div>
            </Link>
          </div>
        </div>

      </main>
    </>
  )
}

