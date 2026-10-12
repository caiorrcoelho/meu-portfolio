from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Caio Ryan | Portfólio</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html {
                scroll-behavior: smooth;
            }

            body {
                font-family: Arial, sans-serif;
                background: #080d18;
                color: #f1f5f9;
            }

            header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 25px 8%;
                background: #101827;
                border-bottom: 1px solid #26364d;
            }

            header h2 {
                color: #38bdf8;
            }

            nav a {
                color: white;
                text-decoration: none;
                margin-left: 20px;
            }

            nav a:hover {
                color: #38bdf8;
            }

            .inicio {
                min-height: 80vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: flex-start;
                padding: 70px 10%;
                background:
                    radial-gradient(ellipse at top right,
                    #12335a 0%, #080d18 65%);
            }

            .inicio p:first-child {
                color: #38bdf8;
                letter-spacing: 3px;
                margin-bottom: 20px;
            }

            .inicio h1 {
                font-size: clamp(38px, 7vw, 68px);
                margin-bottom: 15px;
            }

            .inicio h1 span {
                color: #38bdf8;
            }

            .inicio h3 {
                color: #94a3b8;
                font-size: 23px;
                margin-bottom: 20px;
            }

            .inicio .descricao {
                max-width: 650px;
                line-height: 1.8;
                color: #cbd5e1;
            }

            .botao {
                display: inline-block;
                margin-top: 30px;
                padding: 14px 24px;
                background: #0284c7;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: 0.3s;
            }

            .botao:hover {
                background: #38bdf8;
                color: #080d18;
                transform: translateY(-3px);
            }

            section.conteudo {
                padding: 70px 10%;
            }

            .conteudo h2 {
                font-size: 32px;
                margin-bottom: 25px;
            }

            .conteudo h2 span {
                color: #38bdf8;
            }

            .conteudo p {
                color: #cbd5e1;
                line-height: 1.8;
            }

            .projetos {
                display: grid;
                grid-template-columns:
                    repeat(auto-fit, minmax(220px, 1fr));
                gap: 22px;
            }

            .card {
                background: #101827;
                border: 1px solid #26364d;
                padding: 25px;
                border-radius: 12px;
                transition: 0.3s;
            }

            .card:hover {
                transform: translateY(-5px);
                border-color: #38bdf8;
            }

            .card h3 {
                color: #38bdf8;
                margin-bottom: 12px;
            }

            footer {
                text-align: center;
                padding: 25px;
                background: #101827;
                color: #94a3b8;
            }

            @media (max-width: 600px) {
                header {
                    flex-direction: column;
                    gap: 18px;
                }

                nav a {
                    margin: 0 6px;
                    font-size: 14px;
                }
            }
            /* Animação suave ao carregar a página */
@keyframes aparecer {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

body {
    animation: aparecer 0.8s ease-out both;
}

/* Cartões com movimento e brilho */
.card {
    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease,
        border-color 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(0, 140, 255, 0.18);
    border-color: #168cff;
}

/* Links e botões */
a {
    transition:
        color 0.25s ease,
        background-color 0.25s ease,
        transform 0.25s ease;
}

a:hover {
    color: #60a5fa;
}

/* Entrada progressiva dos títulos */
h1, h2 {
    animation: aparecer 0.8s ease-out both;
}

/* Respeita quem prefere menos movimento */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
        </style>
    </head>

    <body>
        <header>
            <h2>CAIO.DEV</h2>

            <nav>
                <a href="#inicio">Início</a>
                <a href="#sobre">Sobre</a>
                <a href="#habilidades">Habilidades</a>
                <a href="#projetos">Projetos</a>
                <a href="#contato">Contato</a>
            </nav>
        </header>

        <main>
            <section class="inicio" id="inicio">
                <p>PORTFÓLIO DE TECNOLOGIA</p>

                <h1>Olá, eu sou <span>Caio Ryan</span></h1>

                <h3>Estudante de Redes de Computadores</h3>

                <p class="descricao">
                    Estudo na EEMTI Walquer Cavalcante Maia
                    e estou construindo minha jornada no mundo
                    da tecnologia, programação e redes.
                </p>

                <a href="#projetos" class="botao">
                    Conheça meus projetos
                </a>
            </section>

            <section class="conteudo" id="sobre">
                <h2>Sobre <span>mim</span></h2>

                <p>
                    Sou estudante de Redes de Computadores,
                    interessado em programação, infraestrutura,
                    desenvolvimento web e novas tecnologias.
                    Este portfólio é um espaço para apresentar
                    meu aprendizado e meus projetos.
                </p>
            </section>

            <section class="conteudo" id="habilidades">
    <h2>Minhas <span>habilidades</span></h2>

    <div class="projetos">
        <article class="card">
            <h3>Python</h3>
            <p>Aprendendo lógica de programação e desenvolvimento.</p>
        </article>

        <article class="card">
            <h3>HTML e CSS</h3>
            <p>Praticando a criação de páginas para a web.</p>
        </article>

        <article class="card">
            <h3>Redes de Computadores</h3>
            <p>Estudando protocolos, endereçamento IP e redes.</p>
        </article>
    </div>
</section>

            <section class="conteudo" id="projetos">
                <h2>Meus <span>projetos</span></h2>

                <div class="projetos">
                    <article class="card">
                        <h3>Python</h3>
                        <p>
                            Projetos e exercícios para desenvolver
                            minhas habilidades em programação.
                        </p>
                    </article>

                    <article class="card">
                        <h3>Desenvolvimento Web</h3>
                        <p>
                            Criação de páginas utilizando HTML,
                            CSS e Python com Flask.
                        </p>
                    </article>

                    <article class="card">
                        <h3>Redes de Computadores</h3>
                        <p>
                            Estudos sobre redes, protocolos,
                            conectividade e infraestrutura.
                        </p>
                    </article>
                </div>
            </section>

            <section class="conteudo" id="contato">
                <h2>Entre em <span>contato</span></h2>
                <p>
                    Confira meu email e minhas redes e entre em contato
                    comigo:
                </p>

                <div class="projetos">
                    <article class="card">
                        <h3>Email</h3>
                        <p>Entre em contato pelo meu email!</p>
                        <a
                        href="mailto:caiorcdsouza@gmail.com"
                        target="_blank">
                        Enviar Email
                        </a>
                    </article>

                    <article class="card">
                        <h3>Instagram</h3>
                        <p>Acompanhe o meu perfil!.</p>
                        <a
                            href="https://www.instagram.com/caiorrcoelho/"
                            target="_blank"
                            rel="noopener noreferrer">
                            Acessar Instagram
                            </a>
                    </article>

                    <article class="card">
                        <h3>GitHub</h3>
                        <p>Acompanhe o meu Github!.</p>
                        <a 
                            href="https://github.com/caiorrcoelho"
                            target="_blank"
                            rel="noopener noreferrer">
                            Acessar GitHub
                        </a>
                    </article>
                </div>
            </section>
        </main>
        </section>

        <footer>
            <p>© 2026 Caio Ryan | Desenvolvido com Python</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=8000)