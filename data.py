# Todos los datos de la web viven aquí. Edita este archivo y las páginas se actualizan solas.
# Las fotos van en static/img/. Si una foto no existe, la web muestra un recuadro con el nombre.
# VERIFICA siempre autoridades, fechas y cifras en fuentes oficiales (INEC, GAD, Gobernación).

PROVINCIA = {
    "nombre": "Los Ríos",
    "capital": "Babahoyo",
    "region": "Costa (Litoral) del Ecuador",
    "fecha_creacion": "6 de octubre de 1860",
    "poblacion": "Censo INEC 2010: 778 115 habitantes (actualiza con el Censo 2022)",
    "cantones_total": 13,
    "descripcion": (
        "Los Ríos es una provincia de la región Costa del Ecuador, en el centro del litoral. "
        "Su nombre se debe a la gran cantidad de ríos que la atraviesan, entre ellos el Babahoyo, "
        "el Vinces, el Quevedo, el Zapotal y el San Pablo, que forman parte de la cuenca del Guayas. "
        "Sus suelos fértiles la convierten en una de las zonas agrícolas más importantes del país."),
    "historia": (
        "La provincia fue creada por decreto legislativo el 6 de octubre de 1860. "
        "Babahoyo, su capital, es una ciudad fluvial que durante mucho tiempo fue un punto clave "
        "de comercio entre la Sierra y el puerto de Guayaquil. Con los años, el auge del cacao y "
        "luego del banano, el arroz y otros cultivos hizo crecer los cantones de la provincia."),
    "datos": [
        ("Capital", "Babahoyo"),
        ("Creación", "6 de octubre de 1860"),
        ("Cantones", "13"),
        ("Región", "Costa"),
        ("Actividad principal", "Agricultura"),
        ("Cultivos", "Banano, cacao, arroz, maíz, soya, café"),
    ],
    "economia": (
        "La economía se basa en la agricultura: banano, cacao, arroz, maíz duro, soya, café y "
        "maracuyá. También tienen importancia el comercio (sobre todo en Quevedo y Babahoyo), "
        "la ganadería y la agroindustria."),
    "geografia": (
        "Es una región de llanuras y zonas bajas, con clima tropical cálido y húmedo, con una época "
        "lluviosa (invierno) en la que varios ríos pueden desbordarse, y una época seca (verano)."),
    "turismo_general": [
        ("Turismo fluvial y de naturaleza", "Paseos por los ríos, balnearios y haciendas."),
        ("Agroturismo", "Visitas a plantaciones de cacao y banano para conocer cómo se producen."),
        ("Gastronomía", "Cocina costeña con platos como el seco de gallina criolla y la tonga."),
    ],
    "gastronomia_general": [
        "Seco de gallina criolla", "Tonga", "Caldo de manguera", "Bolón de verde",
        "Arroz con menestra y carne asada", "Encebollado de pescado",
    ],
    "bandera": "bandera.png",
    "mapa": "mapa_provincia.png",
}

AUTORIDADES = [
    {
        "cargo": "Prefecto de Los Ríos",
        "nombre": "Jonny Enrique Terán Salcedo",
        "foto": "prefecto.jpg",
        "bio": ("Es el prefecto provincial de Los Ríos, máxima autoridad del Gobierno Autónomo "
                "Descentralizado (GAD) Provincial. Su periodo actual corresponde a 2023-2027. "
                "La prefectura se encarga de obras como vías rurales, riego y fomento productivo "
                "en la provincia."),
        "nota": "Completa la biografía con su profesión y trayectoria desde fuentes oficiales.",
    },
    {
        "cargo": "Gobernador de Los Ríos",
        "nombre": "Galo Lara",
        "foto": "gobernador.jpg",
        "bio": ("Fue designado gobernador de la provincia por el presidente Daniel Noboa mediante el "
                "Decreto Ejecutivo 219, y asumió el cargo el 18 de noviembre de 2025. Antes fue "
                "asambleísta por Los Ríos y es ingeniero en ventas. El gobernador representa al "
                "Gobierno Nacional en la provincia y no es elegido por voto popular, sino designado."),
        "nota": "Los gobernadores cambian con frecuencia: verifica que siga en el cargo.",
    },
]

# slug: datos del cantón. Lo que sea None o vacío se muestra como "Por completar".
CANTONES = {
    "babahoyo": {
        "nombre": "Babahoyo",
        "lema": "Capital de la provincia",
        "descripcion": ("Babahoyo es la capital de Los Ríos. Es una ciudad ribereña, centro "
                        "administrativo, comercial y de servicios de la provincia."),
        "resena": ("Su ubicación junto al río Babahoyo la convirtió desde antiguo en un punto de "
                   "paso entre la Sierra y Guayaquil. Hoy combina comercio, instituciones públicas, "
                   "universidades y una zona rural muy agrícola. En la temporada de lluvias algunos "
                   "sectores se ven afectados por el crecimiento de los ríos."),
        "parroquias": ["Clemente Baquerizo (urbana)", "Dr. Camilo Ponce (urbana)",
                       "Barreiro (urbana)", "El Salto (urbana)", "Caracol (rural)",
                       "Febres Cordero (rural)", "La Unión (rural)", "Pimocha (rural)"],
        "platos": ["Seco de gallina criolla", "Caldo de manguera", "Bolón de verde",
                   "Arroz con menestra y carne asada"],
        "turismo": [("Malecón de Babahoyo", "Es el paseo junto al río, ideal para caminar, ver el atardecer y comer."),
                    ("Ríos y esteros del cantón", "Permiten paseos en canoa y conocer la vida ribereña.")],
        "hoteles": [], "alcalde": None, "poblacion": "153 776 (Censo 2010)",
        "dato_curioso": "Es la capital provincial desde el 30 de septiembre de 1948.",
    },
    "quevedo": {
        "nombre": "Quevedo",
        "lema": "El gran centro comercial de la provincia",
        "descripcion": ("Quevedo es el cantón más poblado de Los Ríos y su principal centro comercial. "
                        "Está en el norte de la provincia, en una zona muy productiva."),
        "resena": ("Creció rápidamente por el comercio de productos agrícolas como banano, cacao, maíz y "
                   "palma. Su ubicación la conecta con la Sierra y otras provincias de la Costa. "
                   "Fue cantonizado el 7 de octubre de 1943."),
        "parroquias": ["Quevedo", "San Camilo", "Guayacán", "Nicolás Infante Díaz", "San Cristóbal",
                       "Siete de Octubre", "24 de Mayo", "Venus del Río Quevedo", "Viva Alfaro",
                       "San Carlos (rural)", "La Esperanza (rural)"],
        "platos": ["Tonga", "Seco de gallina criolla", "Caldo de manguera", "Encebollado"],
        "turismo": [("Río Quevedo", "Es el río que da identidad a la ciudad y a su gente."),
                    ("Parques y plazas del centro", "Son puntos de encuentro y de comercio.")],
        "hoteles": [], "alcalde": None, "poblacion": "173 575 (Censo 2010)",
        "dato_curioso": "Es el cantón más poblado de la provincia.",
    },
    "vinces": {
        "nombre": "Vínces",
        "lema": "La «Pequeña París»",
        "descripcion": ("Vínces es un cantón cacaotero junto al río del mismo nombre, conocido por "
                        "su historia y su patrimonio cultural."),
        "resena": ("En la época del auge del cacao, a finales del siglo XIX y principios del XX, "
                   "familias de hacendados cacaoteros hicieron de Vínces un lugar próspero, por lo que se le "
                   "dio el apodo de «Pequeña París». Aún conserva esa tradición cultural."),
        "parroquias": ["Vinces (urbana)", "Antonio Sotomayor (rural)"],
        "platos": ["Seco de gallina criolla", "Bolón de verde", "Chocolate y derivados del cacao"],
        "turismo": [("Parque Cultural de Vínces", "Reúne espacios culturales y recuerda la historia cacaotera."),
                    ("Río Vínces", "Es el eje de la vida del cantón.")],
        "hoteles": [], "alcalde": None, "poblacion": "71 736 (Censo 2010)",
        "dato_curioso": "Su apodo viene de la riqueza que dejó el cacao.",
    },
    "ventanas": {
        "nombre": "Ventanas",
        "lema": "Tierra de producción agrícola",
        "descripcion": "Cantón del sur de la provincia, con cultivos de banano, cacao y otros productos.",
        "resena": ("Es un cantón comercial y agrícola. Su ubicación lo conecta con Babahoyo y con la vía "
                   "hacia la Sierra y otras provincias."),
        "parroquias": ["Ventanas (urbana)", "Zapotal (urbana)", "Chacarita (rural)", "Los Ángeles (rural)"],
        "platos": ["Seco de gallina criolla", "Caldo de manguera", "Bolón de verde"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": "66 551 (Censo 2010)",
        "dato_curioso": None,
    },
    "baba": {
        "nombre": "Baba",
        "lema": "Tierra de arroz y cacao",
        "descripcion": "Cantón agrícola conocido por sus campos de arroz, cacao y otros cultivos.",
        "resena": "Es un cantón pequeño y tranquilo, cuya vida gira alrededor del trabajo agrícola y los ríos.",
        "parroquias": ["Guare (rural)", "Isla de Bejucal (rural)"],
        "platos": ["Seco de gallina criolla", "Bolón de verde"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
    "buena-fe": {
        "nombre": "Buena Fe",
        "lema": "Agricultura y ganadería",
        "descripcion": "Cantón del norte de la provincia, de producción agrícola y ganadera.",
        "resena": "Su economía depende del campo: banano, cacao, maíz y ganadería, además del comercio local.",
        "parroquias": ["San Jacinto de Buena Fe (urbana)", "Patricia Pilar (rural)"],
        "platos": ["Tonga", "Seco de gallina criolla"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
    "montalvo": {
        "nombre": "Montalvo",
        "lema": "Cantón de la zona sur-central",
        "descripcion": "Cantón agrícola de Los Ríos, con cultivos de arroz, maíz, cacao y otros productos.",
        "resena": None, "parroquias": ["Montalvo (cabecera cantonal)"],
        "platos": ["Seco de gallina criolla", "Bolón de verde"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
    "puebloviejo": {
        "nombre": "Puebloviejo",
        "lema": "Cantón ribereño",
        "descripcion": "Cantón de la zona sur-oeste de la provincia, con producción agrícola.",
        "resena": None, "parroquias": ["Puebloviejo (urbana)", "San Juan (rural)", "Puerto Pechiche (rural)"],
        "platos": ["Seco de gallina criolla", "Caldo de manguera"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
    "urdaneta": {
        "nombre": "Urdaneta",
        "lema": "Cantón agrícola",
        "descripcion": "Cantón con cabecera en Catarama, ubicado cerca del río del mismo nombre.",
        "resena": None, "parroquias": ["Catarama (cabecera)", "Ricaurte (rural)"],
        "platos": ["Seco de gallina criolla", "Caldo de manguera"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
    "palenque": {
        "nombre": "Palenque",
        "lema": "Cantón de la zona central",
        "descripcion": "Cantón agrícola de Los Ríos, de economía basada en el campo.",
        "resena": None, "parroquias": ["Palenque (cabecera cantonal)"],
        "platos": ["Seco de gallina criolla"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
    "valencia": {
        "nombre": "Valencia",
        "lema": "Cantón del norte",
        "descripcion": "Cantón del norte de la provincia, con producción agrícola y ganadera.",
        "resena": None, "parroquias": ["Valencia (cabecera cantonal)"],
        "platos": ["Tonga", "Seco de gallina criolla"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
    "mocache": {
        "nombre": "Mocache",
        "lema": "Cantón agrícola",
        "descripcion": "Cantón de Los Ríos con cultivos de arroz, cacao, maíz y otros productos.",
        "resena": None, "parroquias": ["Mocache (cabecera cantonal)"],
        "platos": ["Seco de gallina criolla", "Bolón de verde"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
    "quinsaloma": {
        "nombre": "Quinsaloma",
        "lema": "Cantón de la zona norte",
        "descripcion": "Cantón agrícola de Los Ríos, con producción de banano, cacao y maíz.",
        "resena": None, "parroquias": ["Quinsaloma (cabecera cantonal)"],
        "platos": ["Tonga", "Seco de gallina criolla"],
        "turismo": [], "hoteles": [], "alcalde": None, "poblacion": None, "dato_curioso": None,
    },
}

# ----------------------------------------------------------------------------
# Reseñas ampliadas (textos descriptivos). Puedes editarlas o reemplazarlas.
# ----------------------------------------------------------------------------
RESENAS = {
    "babahoyo": ("Babahoyo es la capital de la provincia y el corazón administrativo de Los Ríos. "
        "Su ubicación junto al río Babahoyo la convirtió en un punto de paso entre la Sierra y Guayaquil, "
        "y de ahí viene su tradición comercial. Hoy es una ciudad de ritmo tranquilo, con malecón, "
        "mercados, universidades y una amplia zona rural dedicada al arroz, al banano y a otros cultivos. "
        "En invierno, el crecimiento de los ríos obliga a estar atentos a las zonas bajas."),
    "quevedo": ("Quevedo es el cantón más comercial de la provincia. Su gente es emprendedora, y sus calles "
        "se llenan de tiendas, mercados y transporte que conecta la Costa con la Sierra. A su alrededor se "
        "extienden plantaciones de banano, cacao, maíz y palma. Es un buen lugar para conocer la vida "
        "cotidiana de Los Ríos, probar su comida y recorrer la ciudad a pie."),
    "vinces": ("Vínces es uno de los cantones con más historia. Durante el auge del cacao fue un lugar próspero, "
        "y por eso se le conoce con el apodo de «Pequeña París». Aún se aprecia ese pasado en su cultura y "
        "en la importancia del río Vínces para la vida del cantón. Es ideal para quienes buscan historia, "
        "tranquilidad y paisajes de campo."),
    "ventanas": ("Ventanas es un cantón agrícola y comercial del sur de la provincia. Sus cultivos, sobre todo de "
        "banano y cacao, mueven la economía local, y su ubicación facilita el comercio con otras zonas de la "
        "Costa. Es un cantón de gente trabajadora, con ferias y mercados donde se encuentra producto fresco."),
    "baba": ("Baba es un cantón pequeño y tranquilo, rodeado de campos de arroz, cacao y otros cultivos. "
        "Aquí el paisaje lo definen los ríos, los esteros y el trabajo del campo. Es un buen lugar para "
        "conocer la vida rural y el origen de muchos productos de la provincia."),
    "buena-fe": ("Buena Fe es un cantón del norte de la provincia, en una zona de tierras fértiles. Su economía "
        "depende de la agricultura y la ganadería, con cultivos como banano, cacao y maíz. Es un cantón "
        "en crecimiento, cercano a Quevedo, con mucho movimiento comercial."),
    "montalvo": ("Montalvo es un cantón de vocación agrícola, donde el arroz, el maíz y el cacao marcan el ritmo "
        "del año. Sus campos, ríos y caminos rurales ofrecen un ambiente apacible y muy típico de la "
        "Costa ecuatoriana."),
    "puebloviejo": ("Puebloviejo es un cantón ribereño, donde los ríos y esteros son parte de la vida diaria. "
        "La agricultura es la base de su economía, y sus paisajes de campo y agua son muy característicos "
        "de la zona baja de la provincia."),
    "urdaneta": ("Urdaneta tiene su cabecera en Catarama y se ubica cerca de ríos importantes de la provincia. "
        "Su gente vive principalmente de la agricultura y del comercio local. Es un cantón tranquilo, con "
        "paisajes verdes y una fuerte identidad rural."),
    "palenque": ("Palenque es un cantón agrícola del centro de la provincia. Sus campos producen cultivos típicos "
        "de la Costa y su comunidad mantiene costumbres campesinas muy arraigadas."),
    "valencia": ("Valencia es un cantón del norte de Los Ríos, en una zona de agricultura y ganadería. "
        "Sus tierras producen banano, maíz y cacao, y su ubicación lo conecta con otros cantones "
        "productivos de la región."),
    "mocache": ("Mocache es un cantón agrícola donde el arroz, el maíz y el cacao son protagonistas. "
        "Su territorio plano y sus ríos favorecen la producción, y su vida comunitaria gira alrededor "
        "del campo."),
    "quinsaloma": ("Quinsaloma es un cantón agrícola del norte de la provincia, con cultivos de banano, cacao y "
        "maíz. Su ambiente rural y sus paisajes verdes lo convierten en un lugar tranquilo, vinculado "
        "al trabajo del campo."),
}

import urllib.parse as _u
for _slug, _c in CANTONES.items():
    if _slug in RESENAS:
        _c["resena"] = RESENAS[_slug]
    _c["mapa_q"] = f'{_c["nombre"]}, Los Ríos, Ecuador'
    _c["hoteles_url"] = "https://www.google.com/maps/search/" + _u.quote(f'hoteles en {_c["nombre"]}, Los Ríos, Ecuador')
PROVINCIA["mapa_q"] = "Provincia de Los Ríos, Ecuador"
