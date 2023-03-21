import Link from 'next/link'
import Image from 'next/image'
import { useState } from 'react'

const NavBar = () => {
    const [navActive, setNavActive] = useState(0);
    console.log(navActive)
    return (
        <header>
            <nav className='navbarcontainer'>
                <Link href="/">
                    <h1>
                        Cellier
                    </h1>
                </Link>
                <div className='btncellier'
                    onClick={() =>
                        setNavActive(navActive)}>
                    <Link href="/">
                        <Image
                            src="/settings.png"
                            alt="settings"
                            className='vercelLogo3'
                            width={512}
                            height={512}
                            priority
                        />
                    </Link>
                    <Link href="/">
                        <Image
                            src="/usuario.png"
                            alt="usuario"
                            className='vercelLogo2'
                            width={512}
                            height={512}
                            priority
                        />
                    </Link>
                    <Image
                        src="/cellier-logo-square.png"
                        alt="cellier-logo-square"
                        className='vercelLogo1'
                        width={512}
                        height={512}
                        priority
                    />
                </div>
            </nav>
        </header>
    );
}
export default NavBar