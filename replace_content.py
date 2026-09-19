import re

def update_english():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Title and metadata
    content = content.replace('<title>Fer Mavec | AI Researcher, Analyst & Technical Writer</title>', '<title>Fer Mavec | AI, Intelligence & Philosophy</title>')
    content = content.replace('"jobTitle": "AI Researcher, Analyst & Technical Writer",', '"jobTitle": "Independent Researcher and Writer",')
    content = content.replace('content="Fer Mavec: AI Researcher, Analyst & Technical Writer. Investigating how artificial intelligence reshapes cognition, behavior and society."', 'content="Fer Mavec: Independent researcher and writer working at the intersection of artificial intelligence, cognition, and philosophy."')
    
    # Header Nav
    content = content.replace('<li><a href="#services">What I can do for you</a></li>', '<li><a href="#services">Work</a></li>')

    # 2. Hero
    hero_old = '''<h1 style="margin-bottom: 1.2rem;">AI Researcher, Analyst <span class="highlight">& Technical Writer</span></h1>
                <p style="font-size: 1.1rem; color: var(--text-secondary); line-height: 1.6; font-weight: 400; margin: 0 0 2.5rem;">I work at the frontier between artificial intelligence and the people who live it.</p>'''
    hero_new = '''<h1 style="margin-bottom: 1.2rem;">AI, Intelligence <span class="highlight">& Philosophy</span></h1>
                <p style="font-size: 1.1rem; color: var(--text-secondary); line-height: 1.6; font-weight: 400; margin: 0 0 2.5rem;">Independent research and writing on artificial intelligence, cognition, and the problem of attributing intelligence.</p>'''
    content = content.replace(hero_old, hero_new)

    # 3. About
    about_old = '''        <!-- PRESERVED: About / Profile Section (bio content not included in new design)
        <section id="about" style="padding-bottom: 2rem;">'''
    about_new = '''        <section id="about" style="padding-bottom: 2rem;">
            <div class="container">
                <h2 class="section-title">About Me</h2>
                <div class="about-text" style="max-width: 800px;">
                    <p class="lead">I am an independent researcher and writer working at the intersection of artificial intelligence, cognition, and philosophy. With a technical background in data science and AI, I investigate how we define intelligence and when—if ever—we are justified in attributing it to artificial systems.</p>
                    <p>My technical background includes being a Project Management Engineer, a Specialist in Data Science and AI projects, and currently finishing a Master's in Data Science and AI.</p>
                    <p><em>“Before asserting that a machine thinks—or that it never will—we must clarify what intelligence means, what evidence we count as relevant, and under what criteria we make that attribution.”</em></p>
                </div>
            </div>
        </section>
        
        <!-- PRESERVED: About / Profile Section (bio content not included in new design)
        <section id="about-old" style="padding-bottom: 2rem;">'''
    content = content.replace(about_old, about_new)

    # 4. Services / Work
    services_old = '''<h2 class="section-title">What I can do for you</h2>
                <div class="projects-grid" style="margin-top: 2rem;">

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Technical & Executive Writing</h3>
                        <p>Technical documents, whitepapers, executive ghostwriting and B2B content that translates complex AI and technology topics into clear, high-impact communication for decision-makers.</p>
                        <div style="margin-top: auto; padding-top: 1.5rem;">
                            <a href="https://drive.google.com/file/d/1XW4Af4xb0h9jg5Q_dGcjy36ZbeaQCKG8/view" target="_blank" rel="noopener noreferrer" class="btn-secondary" style="display: inline-flex; align-items: center; gap: 0.4rem;">
                                <i class="fas fa-download"></i> Download Portfolio (PDF)
                            </a>
                        </div>
                    </div>

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Accessibility Auditing <span style="font-size: 0.85rem; font-weight: 400; color: var(--text-secondary);">(Vision-centered)</span></h3>
                        <p>End-to-end accessibility audits for digital products, focused on low vision and visual impairment. Combines automated detection with real-user experience and references WCAG 2.2 and international accessibility standards.</p>
                        <div style="margin-top: auto; padding-top: 1.5rem;">
                            <a href="https://drive.google.com/file/d/1ZU5Cx8Axi7qR3yFEDgPRVImDA7pfHcTJ/view?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-secondary">
                                See demo
                            </a>
                        </div>
                    </div>

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Responsible AI Consulting & Governance</h3>
                        <p>Advisory and implementation for organizations adopting AI responsibly — ethics frameworks, ISO standards, risk assessment and human-centered governance. Includes an AI Readiness diagnostic with senior leadership.</p>
                        <div style="margin-top: auto; padding-top: 1.5rem;">
                            <a href="mailto:fermavec@gmail.com?subject=Responsible%20AI%20Consulting" class="btn-secondary">
                                Send me an email
                            </a>
                        </div>
                    </div>

                </div>'''
    services_new = '''<h2 class="section-title">Work</h2>
                <div class="projects-grid" style="margin-top: 2rem;">

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Writing, Analysis & AI Research</h3>
                        <p>Essays, context analysis, documentary research, and technical writing on artificial intelligence for media, editorial projects, organizations, and audiences seeking to understand the topic with rigor and clarity.</p>
                    </div>

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Conversations & Collaborations</h3>
                        <p>Available for interviews, podcasts, public conversations, and editorial collaborations on AI, cognition, philosophy of mind, epistemology, and tech culture.</p>
                    </div>

                </div>'''
    content = content.replace(services_old, services_new)

    # 5. Perspective & Research
    perspective_old = '''<p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin-bottom: 3rem; line-height: 1.6;">My applied work is informed by an active research perspective on the human and social impact of AI — across accessibility, governance, cognition and the sociotechnical dimensions of intelligent systems.</p>

                <h3 style="font-size: 1.4rem; font-weight: 600; margin-bottom: 2rem; letter-spacing: -0.02em;">Research Themes</h3>
                <div class="research-grid" style="margin-bottom: 4rem;">
                    <div class="research-item">
                        <h4>Human-Centered Systems</h4>
                        <p>Systems designed to align with and amplify human cognition and functional utility.</p>
                    </div>
                    <div class="research-item">
                        <h4>Accessibility & Inclusive Design</h4>
                        <p>Multimodal interfaces and adaptive technologies for diverse cognitive and physical needs.</p>
                    </div>
                    <div class="research-item">
                        <h4>Responsible AI & Governance</h4>
                        <p>Frameworks for ethical deployment, risk mitigation, and systemic accountability.</p>
                    </div>
                    <div class="research-item">
                        <h4>Human-AI Interaction</h4>
                        <p>Study of behavioral dynamics, trust, and communication in synthetic-human partnerships.</p>
                    </div>
                    <div class="research-item">
                        <h4>AI & Society</h4>
                        <p>Broader impacts of intelligent automation on culture, labor, and social structures.</p>
                    </div>
                </div>

                <div class="blog-header">
                    <h3 style="font-size: 1.4rem; font-weight: 600; margin-bottom: 0.5rem; letter-spacing: -0.02em;">Essays & Research</h3>
                    <p class="section-subtitle">Curated archive of independent research, technical essays and socio-technical analysis.</p>
                </div>

                <div class="blog-intro-text">
                    <p>This space features long-form analysis and research notes exploring the intersection of artificial intelligence, cognition, accessibility, and human behavior.</p>
                </div>

                <div class="newsletter-cta" style="background: transparent; border: 1px solid var(--border-color, #333); border-radius: 6px; padding: 1.2rem 1.5rem; margin: 2rem 0; display: flex; flex-direction: column; align-items: flex-start; text-align: left; width: 100%;">
                    <div style="font-size: 0.7rem; font-weight: 600; color: var(--accent-color, #00f0ff); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;"><i class="fas fa-lock" style="margin-right: 4px;"></i> Research Essays on AI, Accessibility and Human-Centered Systems</div>
                    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; width: 100%; gap: 1rem;">
                        <div style="flex: 1 1 300px;">
                            <h3 style="font-size: 1.1rem; margin-bottom: 0.2rem;">Independent Research & Analysis</h3>
                            <p style="font-size: 0.85rem; color: var(--text-secondary, #888); margin: 0; line-height: 1.4;">Subscribe to Substack for deep-dive technical essays and socio-technical analysis.</p>
                        </div>'''
    perspective_new = '''<p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin-bottom: 3rem; line-height: 1.6;">My research explores the conceptual and philosophical foundations of artificial intelligence.</p>

                <h3 style="font-size: 1.4rem; font-weight: 600; margin-bottom: 2rem; letter-spacing: -0.02em;">Research Themes</h3>
                <div class="research-grid" style="margin-bottom: 4rem;">
                    <div class="research-item">
                        <h4>Intelligence & Attribution</h4>
                        <p>How intelligence has been defined, what criteria we use to recognize it, and what changes when the agent is non-biological.</p>
                    </div>
                    <div class="research-item">
                        <h4>Minds, Machines & Cognition</h4>
                        <p>Philosophy of mind, consciousness, intentionality, functionalism, and the limits of comparing AI models to human minds.</p>
                    </div>
                    <div class="research-item">
                        <h4>Epistemology of AI</h4>
                        <p>Epistemic opacity, evidence, explanation, reliability, and the limits of what we know about complex artificial systems.</p>
                    </div>
                    <div class="research-item">
                        <h4>Philosophy of Science & AI</h4>
                        <p>Abduction, explanation, demarcation, and criteria to separate evidence, marketing, prediction, and knowledge.</p>
                    </div>
                    <div class="research-item">
                        <h4>AI Narratives & Public Understanding</h4>
                        <p>How labs, companies, media, and governments present the capabilities and future of AI.</p>
                    </div>
                </div>

                <div class="blog-header">
                    <h3 style="font-size: 1.4rem; font-weight: 600; margin-bottom: 0.5rem; letter-spacing: -0.02em;">Essays & Archive</h3>
                    <p class="section-subtitle">Essays, research notes, and rigorous popularization on AI, intelligence, and philosophy.</p>
                </div>

                <div class="blog-intro-text">
                    <p><em>This archive documents independent work in progress. It is not a substitute for peer-reviewed academic research.</em></p>
                </div>

                <div class="newsletter-cta" style="background: transparent; border: 1px solid var(--border-color, #333); border-radius: 6px; padding: 1.2rem 1.5rem; margin: 2rem 0; display: flex; flex-direction: column; align-items: flex-start; text-align: left; width: 100%;">
                    <div style="font-size: 0.7rem; font-weight: 600; color: var(--accent-color, #00f0ff); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;"><i class="fas fa-lock" style="margin-right: 4px;"></i> Research Essays on AI, Intelligence and Philosophy</div>
                    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; width: 100%; gap: 1rem;">
                        <div style="flex: 1 1 300px;">
                            <h3 style="font-size: 1.1rem; margin-bottom: 0.2rem;">Independent Research & Analysis</h3>
                            <p style="font-size: 0.85rem; color: var(--text-secondary, #888); margin: 0; line-height: 1.4;">Subscribe to Substack for deep-dive technical essays and philosophical analysis.</p>
                        </div>'''
    content = content.replace(perspective_old, perspective_new)

    # 6. Contact
    contact_old = '''<p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 500px; margin: 0 auto 2.5rem; line-height: 1.6;">If you have a project, idea or challenge that could use a sharp perspective — let's talk.</p>'''
    contact_new = '''<p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 500px; margin: 0 auto 2.5rem; line-height: 1.6;">Available for interviews, public conversations, editorial collaborations, and research/writing projects related to AI and intelligence.</p>'''
    content = content.replace(contact_old, contact_new)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)


def update_spanish():
    with open('es.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Title and metadata
    content = content.replace('<title>Fer Mavec | Investigador en IA, Analista y Escritor Técnico</title>', '<title>Fer Mavec | IA, inteligencia y filosofía</title>')
    content = content.replace('"jobTitle": "Investigador en IA, Analista y Escritor Técnico",', '"jobTitle": "Investigador y escritor independiente",')
    content = content.replace('content="Fer Mavec: Investigador en IA, Analista y Escritor Técnico. Investigando cómo la inteligencia artificial transforma la cognición, el comportamiento y la sociedad."', 'content="Fer Mavec: Investigador y escritor independiente que trabaja en la intersección de la inteligencia artificial, la cognición y la filosofía."')
    
    # Header Nav
    content = content.replace('<li><a href="#services">Qué puedo hacer por ti</a></li>', '<li><a href="#services">Trabajo</a></li>')

    # 2. Hero
    hero_old = '''<h1 style="margin-bottom: 1.2rem;">Investigador en IA, Analista <span class="highlight">& Escritor Técnico</span></h1>
                <p style="font-size: 1.1rem; color: var(--text-secondary); line-height: 1.6; font-weight: 400; margin: 0 0 2.5rem;">Trabajo en la frontera entre la inteligencia artificial y las personas que la viven.</p>'''
    hero_new = '''<h1 style="margin-bottom: 1.2rem;">IA, inteligencia <span class="highlight">y filosofía</span></h1>
                <p style="font-size: 1.1rem; color: var(--text-secondary); line-height: 1.6; font-weight: 400; margin: 0 0 2.5rem;">Investigación y escritura independiente sobre inteligencia artificial, cognición y el problema de atribuir inteligencia.</p>'''
    content = content.replace(hero_old, hero_new)

    # 3. About
    about_old = '''        <!-- PRESERVED: Sección About / Perfil (contenido del bio no incluido en el nuevo diseño)
        <section id="about" style="padding-bottom: 2rem;">'''
    about_new = '''        <section id="about" style="padding-bottom: 2rem;">
            <div class="container">
                <h2 class="section-title">Sobre mí</h2>
                <div class="about-text" style="max-width: 800px;">
                    <p class="lead">Soy un investigador y escritor independiente que trabaja en la intersección de la inteligencia artificial, la cognición y la filosofía. Con formación técnica en ciencia de datos e IA, investigo cómo definimos la inteligencia y cuándo —si alguna vez— estamos justificados en atribuírsela a sistemas artificiales.</p>
                    <p>Mi formación incluye: Ingeniero en Gestión de Proyectos, Especialista en desarrollo de proyectos de Ciencia de Datos e Inteligencia Artificial, y actualmente concluyendo una maestría en Ciencia de Datos e Inteligencia Artificial.</p>
                    <p><em>“Antes de afirmar que una máquina piensa —o que nunca podrá hacerlo— debemos aclarar qué significa inteligencia, qué evidencia contamos como relevante y bajo qué criterios hacemos esa atribución.”</em></p>
                </div>
            </div>
        </section>
        
        <!-- PRESERVED: Sección About / Perfil (contenido del bio no incluido en el nuevo diseño)
        <section id="about-old" style="padding-bottom: 2rem;">'''
    content = content.replace(about_old, about_new)

    # 4. Services / Work
    services_old = '''<h2 class="section-title">Qué puedo hacer por ti</h2>
                <div class="projects-grid" style="margin-top: 2rem;">

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Technical & Executive Writing</h3>
                        <p>Documentos técnicos, whitepapers, ghostwriting ejecutivo y contenido B2B que traduce temas complejos de IA y tecnología en comunicación clara y de alto impacto para tomadores de decisión.</p>
                        <div style="margin-top: auto; padding-top: 1.5rem;">
                            <a href="https://drive.google.com/file/d/1XW4Af4xb0h9jg5Q_dGcjy36ZbeaQCKG8/view" target="_blank" rel="noopener noreferrer" class="btn-secondary" style="display: inline-flex; align-items: center; gap: 0.4rem;">
                                <i class="fas fa-download"></i> Descargar Portafolio (PDF)
                            </a>
                        </div>
                    </div>

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Accessibility Auditing <span style="font-size: 0.85rem; font-weight: 400; color: var(--text-secondary);">(Vision-centered)</span></h3>
                        <p>Auditorías de accesibilidad integral para productos digitales, con enfoque en baja visión y discapacidad visual. Combina detección automatizada con experiencia de usuario real y referencia a WCAG 2.2 y normativas internacionales de accesibilidad.</p>
                        <div style="margin-top: auto; padding-top: 1.5rem;">
                            <a href="https://drive.google.com/file/d/1ZU5Cx8Axi7qR3yFEDgPRVImDA7pfHcTJ/view?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-secondary">
                                Ver demo
                            </a>
                        </div>
                    </div>

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Responsible AI Consulting & Governance</h3>
                        <p>Asesoría e implementación para organizaciones que adoptan IA de forma responsable — marcos éticos, normas ISO, evaluación de riesgos y gobernanza centrada en el humano. Incluye un diagnóstico de madurez en IA con la alta gerencia.</p>
                        <div style="margin-top: auto; padding-top: 1.5rem;">
                            <a href="mailto:fermavec@gmail.com?subject=Responsible%20AI%20Consulting" class="btn-secondary">
                                Escríbeme
                            </a>
                        </div>
                    </div>

                </div>'''
    services_new = '''<h2 class="section-title">Trabajo</h2>
                <div class="projects-grid" style="margin-top: 2rem;">

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Escritura, análisis e investigación sobre IA</h3>
                        <p>Ensayos, análisis de contexto, investigación documental y escritura técnica sobre inteligencia artificial para medios, proyectos editoriales, organizaciones y audiencias que buscan entender el tema con rigor y claridad.</p>
                    </div>

                    <div class="project-card" style="display: flex; flex-direction: column;">
                        <h3>Conversaciones y colaboraciones</h3>
                        <p>Disponible para entrevistas, podcasts, conversaciones públicas y colaboraciones editoriales sobre IA, cognición, filosofía de la mente, epistemología y cultura tecnológica.</p>
                    </div>

                </div>'''
    content = content.replace(services_old, services_new)

    # 5. Perspective & Research
    perspective_old = '''<p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin-bottom: 3rem; line-height: 1.6;">Mi trabajo aplicado está informado por una perspectiva de investigación activa sobre el impacto humano y social de la IA — en accesibilidad, gobernanza, cognición y las dimensiones sociotécnicas de los sistemas inteligentes.</p>

                <h3 style="font-size: 1.4rem; font-weight: 600; margin-bottom: 2rem; letter-spacing: -0.02em;">Temas de Investigación</h3>
                <div class="research-grid" style="margin-bottom: 4rem;">
                    <div class="research-item">
                        <h4>Sistemas Centrados en el Humano</h4>
                        <p>Sistemas diseñados para alinearse y amplificar la cognición humana y la utilidad funcional.</p>
                    </div>
                    <div class="research-item">
                        <h4>Accesibilidad y Diseño Inclusivo</h4>
                        <p>Interfaces multimodales y tecnologías adaptativas para diversas necesidades cognitivas y físicas.</p>
                    </div>
                    <div class="research-item">
                        <h4>IA Responsable y Gobernanza</h4>
                        <p>Marcos para el despliegue ético, mitigación de riesgos y rendición de cuentas sistémica.</p>
                    </div>
                    <div class="research-item">
                        <h4>Interacción Humano-IA</h4>
                        <p>Estudio de dinámicas de comportamiento, confianza y comunicación en asociaciones sintético-humanas.</p>
                    </div>
                    <div class="research-item">
                        <h4>IA y Sociedad</h4>
                        <p>Impactos más amplios de la automatización inteligente en la cultura, el trabajo y las estructuras sociales.</p>
                    </div>
                </div>

                <div class="blog-header">
                    <h3 style="font-size: 1.4rem; font-weight: 600; margin-bottom: 0.5rem; letter-spacing: -0.02em;">Ensayos & Investigación</h3>
                    <p class="section-subtitle">Archivo de investigación independiente, ensayos técnicos y análisis socio-técnico.</p>
                </div>

                <div class="blog-intro-text">
                    <p>Este espacio destaca análisis extensos y notas de investigación explorando la intersección de la inteligencia artificial, la cognición, la accesibilidad y el comportamiento humano.</p>
                </div>

                <div class="newsletter-cta" style="background: transparent; border: 1px solid var(--border-color, #333); border-radius: 6px; padding: 1.2rem 1.5rem; margin: 2rem 0; display: flex; flex-direction: column; align-items: flex-start; text-align: left; width: 100%;">
                    <div style="font-size: 0.7rem; font-weight: 600; color: var(--accent-color, #00f0ff); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;"><i class="fas fa-lock" style="margin-right: 4px;"></i> Ensayos sobre IA, Accesibilidad y Sistemas Centrados en Humanos</div>
                    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; width: 100%; gap: 1rem;">
                        <div style="flex: 1 1 300px;">
                            <h3 style="font-size: 1.1rem; margin-bottom: 0.2rem;">Investigación y Análisis Independiente</h3>
                            <p style="font-size: 0.85rem; color: var(--text-secondary, #888); margin: 0; line-height: 1.4;">Únete a mi Substack para explorar ensayos técnicos y análisis socio-técnico.</p>
                        </div>'''
    perspective_new = '''<p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 800px; margin-bottom: 3rem; line-height: 1.6;">Mi investigación explora los fundamentos conceptuales y filosóficos de la inteligencia artificial.</p>

                <h3 style="font-size: 1.4rem; font-weight: 600; margin-bottom: 2rem; letter-spacing: -0.02em;">Temas de Investigación</h3>
                <div class="research-grid" style="margin-bottom: 4rem;">
                    <div class="research-item">
                        <h4>Inteligencia y atribución</h4>
                        <p>Cómo se ha definido la inteligencia, qué criterios usamos para reconocerla y qué cambia cuando el agente no es biológico.</p>
                    </div>
                    <div class="research-item">
                        <h4>Mentes, máquinas y cognición</h4>
                        <p>Filosofía de la mente, conciencia, intencionalidad, funcionalismo y los límites de comparar modelos de IA con mentes humanas.</p>
                    </div>
                    <div class="research-item">
                        <h4>Epistemología de la IA</h4>
                        <p>Opacidad epistémica, evidencia, explicación, fiabilidad y los límites de lo que sabemos sobre sistemas artificiales complejos.</p>
                    </div>
                    <div class="research-item">
                        <h4>Filosofía de la ciencia e IA</h4>
                        <p>Abducción, explicación, demarcación y criterios para separar evidencia, marketing, predicción y conocimiento.</p>
                    </div>
                    <div class="research-item">
                        <h4>Narrativas de IA y comprensión pública</h4>
                        <p>Cómo laboratorios, empresas, medios y gobiernos presentan las capacidades y el futuro de la IA.</p>
                    </div>
                </div>

                <div class="blog-header">
                    <h3 style="font-size: 1.4rem; font-weight: 600; margin-bottom: 0.5rem; letter-spacing: -0.02em;">Ensayos & Archivo</h3>
                    <p class="section-subtitle">Ensayos, notas de investigación y divulgación rigurosa sobre IA, inteligencia y filosofía.</p>
                </div>

                <div class="blog-intro-text">
                    <p><em>Este archivo documenta trabajo independiente en desarrollo; no sustituye la investigación académica revisada por pares.</em></p>
                </div>

                <div class="newsletter-cta" style="background: transparent; border: 1px solid var(--border-color, #333); border-radius: 6px; padding: 1.2rem 1.5rem; margin: 2rem 0; display: flex; flex-direction: column; align-items: flex-start; text-align: left; width: 100%;">
                    <div style="font-size: 0.7rem; font-weight: 600; color: var(--accent-color, #00f0ff); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;"><i class="fas fa-lock" style="margin-right: 4px;"></i> Ensayos sobre IA, Inteligencia y Filosofía</div>
                    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; width: 100%; gap: 1rem;">
                        <div style="flex: 1 1 300px;">
                            <h3 style="font-size: 1.1rem; margin-bottom: 0.2rem;">Investigación y Análisis Independiente</h3>
                            <p style="font-size: 0.85rem; color: var(--text-secondary, #888); margin: 0; line-height: 1.4;">Únete a mi Substack para explorar ensayos técnicos y análisis filosófico.</p>
                        </div>'''
    content = content.replace(perspective_old, perspective_new)

    # 6. Contact
    contact_old = '''<p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 500px; margin: 0 auto 2.5rem; line-height: 1.6;">Si tienes un proyecto, una idea o un reto que necesita una perspectiva sólida — hablemos.</p>'''
    contact_new = '''<p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 500px; margin: 0 auto 2.5rem; line-height: 1.6;">Disponible para entrevistas, conversaciones públicas, colaboraciones editoriales y proyectos de investigación/escritura relacionados con IA e inteligencia.</p>'''
    content = content.replace(contact_old, contact_new)

    with open('es.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_english()
update_spanish()
