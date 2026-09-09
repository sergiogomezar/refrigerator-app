# Análisis de viabilidad

Fecha: 4 de septiembre de 2026. Alcance: viabilidad, mercado, competencia, hardware, argumentos de
venta y límites legales. No cubre arquitectura ni decisiones de software, por indicación expresa.

Revisión de mercado: 9 de septiembre de 2026. Se rehízo la sección 4 completa y se ajustaron el
veredicto, la sección 2 y la sección 9. El resto del documento sigue vigente tal como se escribió.

## Veredicto

Vale prototiparla. El problema tiene tamaño verificable: la EPA calculó en abril de 2025 que una
familia de cuatro desperdicia cerca de USD 3 000 de comida al año, alrededor del 17% de lo que
consume el hogar. Nada de lo planteado es técnicamente difícil en 2026.

El riesgo no es técnico, es de retención. Las apps de inventario de cocina no mueren porque no
funcionen: mueren porque el inventario se desactualiza. La idea resuelve bien la *entrada* de datos
(voz y ticket) y no resuelve la *salida*: nadie va a registrar que se comió medio pollo. Un
inventario con 60% de exactitud vuelve inútiles la gestión de caducidad, las recetas y las
sugerencias de compra al mismo tiempo, porque las tres leen del mismo estado.

La salida está dentro de la propia lista de features: convertir la sugerencia de recetas en el
mecanismo de descarga. "Cociné esta receta" con un toque descuenta sus ingredientes.

Corrección de la revisión del 9 de septiembre de 2026: ese mecanismo ya no es una idea disponible.
Durante 2025 y 2026 entró una oleada de apps de despensa con IA que lo trae de fábrica, y varias lo
usan como argumento principal de venta. El detalle está en la sección 4. La consecuencia para el
veredicto es que la apuesta se mueve de "resolvemos la descarga de inventario" a tres cosas que la
oleada no tiene juntas: verdad determinista declarada, datos de producto y ticket latinoamericanos,
y cierre de la compra en un canal local. Sigue valiendo la pena prototiparla; el argumento cambió.

## 1. Qué tan viable es

| Eje | Valoración | Nota |
|---|---|---|
| Factibilidad técnica | Alta | Voz a ítems estructurados y OCR de tickets están resueltos. |
| Tamaño del problema | Alta | 17% del consumo del hogar; ~USD 3 000 al año por familia de cuatro. |
| Retención B2C | Baja | El eje que mata la categoría. Depende de la descarga de inventario. |
| Pago del consumidor | Baja | Ahorrar USD 56 a la semana no convence si cuesta 2 minutos diarios. |
| Pago B2B | Alta | Restaurantes y hoteles ya pagan por merma y por cumplimiento sanitario. |
| Defensibilidad | Media-baja | No está en el algoritmo, sino en datos locales por país. Bajó: la barrera de entrada al resto del producto es casi cero y en 2026 hay una decena de apps nuevas que lo demuestran. |
| Riesgo regulatorio | Medio-alto | Sube fuerte si se implementan datos clínicos. |

Lo que sí es difícil:

- **Normalizar productos.** El ticket dice `LCH ENT DSL 1L` y la base necesita "leche entera, 1 L".
  Ese diccionario, por cadena y por país, es trabajo manual continuo, y es también el activo que
  nadie copia rápido.
- **Cobertura de códigos de barras en Latinoamérica.** Las bases abiertas están sesgadas a Europa y
  Estados Unidos. Muchas marcas propias de cadenas locales no existen en ninguna base.
- **Cantidades, no solo presencia.** Saber que "hay pollo" es fácil; saber que quedan 300 g es lo que
  hace creíbles las recetas y la lista de compras.
- **Costo variable por usuario.** Cada nota de voz, cada ticket y cada tanda de recetas es una
  llamada de modelo. Con usuarios que no pagan, ese costo define si el producto existe.

## 2. Potencial: hogar frente a restaurantes y hoteles

| Dimensión | Familias | Restaurantes y hoteles |
|---|---|---|
| Qué le duele | Tirar comida, no saber qué cocinar | Costo de alimentos, merma, inspección sanitaria |
| Quién decide | Una persona, en dos minutos | Chef ejecutivo, gerente de operaciones, compras |
| Ticket | USD 0–5 al mes | USD 50–500 al mes por sede |
| Ciclo de venta | Instantáneo | 1 a 6 meses, con piloto |
| Precisión exigida | Aproximado sirve | Auditable, con responsable y hora |
| Competencia | Decenas de apps con IA, la mayoría gratuitas o de USD 5–10 al mes | Winnow, Orbisk, Leanpath, Kitro por cotización; MarketMan y Apicbase en software de costo |
| Rol de las recetas | Central | Irrelevante: el menú ya está fijado |

El producto que compra un restaurante no es "recetas con lo que tienes": es etiquetado FEFO,
bitácora de temperatura y costo de merma.

Dónde está el hueco real: los sistemas de merma con cámara reportan retornos de 1,1 a 1,8 meses y
ahorros cercanos a EUR 72 000 por sede al año, pero se venden por cotización a grupos multi-sede.
El restaurante mediano latinoamericano queda fuera por precio. Ese segmento, de 3 a 20 sedes, es
atendible con teléfono, etiquetas y un sensor de USD 20, no con visión artificial.

Matiz de la revisión del 9 de septiembre de 2026: el hueco existe, pero el techo de precio es más
bajo de lo que decía este documento. MarketMan publica USD 199 al mes y cubre control de inventario
teórico contra real, que es la mitad del argumento. Apicbase atiende multi-sede con recetas, stock y
proveedores, aunque también por cotización. Lo que sigue sin cubrirse para 3 a 20 sedes en América
Latina es la combinación de FEFO por lote con etiqueta impresa, bitácora de temperatura y merma con
motivo y responsable, todo desde el teléfono y en español. Ese es el hueco, no "software de
inventario para restaurantes" a secas.

Lectura: el hogar es el mercado de crecimiento y el B2B es el mercado de ingreso. No en la versión 1
y probablemente no con el mismo equipo comercial.

## 3. Falencias y mejoras

Falencias:

1. No hay mecanismo de descarga de inventario. Es la falla estructural.
2. Se promete estimar vida útil según la temperatura sin fuente de temperatura.
3. No se contempla la fecha de apertura del envase, que cambia la vida útil por completo.
4. Los datos clínicos meten el producto en territorio regulado y hacen crítico para la seguridad un
   filtro de alérgenos que depende de datos de composición que casi ningún catálogo tiene completos.
5. Se asume que existen alimentos "globalmente considerados principales". No existen.
6. Se asume que las plataformas de domicilio tienen integración auto-servicio. No la tienen.
7. Multipaís choca con datos de producto por país: códigos, nombres, etiquetado, cadenas.

Mejoras que cambiarían el producto:

- Reencuadrar: no es una app de inventario, es una lista de compras que se vuelve inteligente.
- "Cociné esto" como descarga de un toque.
- Registro de desperdicio con contador de dinero.
- El ticket como vía principal y la voz como excepción.
- Sobras como ítem de primera clase, con caducidad por defecto de tres días.
- WhatsApp antes que app: una nota de voz a un número es fricción cero y cero instalación.

## 4. Competencia y factor diferencial

Revisado el 9 de septiembre de 2026. La versión anterior de esta sección describía el mercado de
2024 y quedó desactualizada: entre 2025 y 2026 apareció una oleada de apps de despensa con IA que
cubren casi todo lo que este producto plantea como propio.

### 4.1 La oleada nueva (2025–2026)

| Quién | Qué hace | Dónde está flojo |
|---|---|---|
| Pantry Persona | Capa de memoria de cocina dentro de ChatGPT y Claude. Voz, hasta 8 perfiles del hogar, alergias y marcas preferidas, recetas, plan de 7 a 30 días, lista compartida. Descarga por conversación: "we had the chicken tonight" y el ítem sale del inventario. Gratis el núcleo; Pro USD 7,99 al mes | No sincroniza precios de tienda ni cuentas de fidelidad. Depende de tener una suscripción a un asistente; la voz solo en plan de pago. Sin OCR de ticket latinoamericano |
| Despify (español) | OCR de ticket, comandos de voz y texto, Modo Inmersivo que guía el cocinado paso a paso, Chef IA, Cooked Mode. Gratis con plan premium | Enfocada a España. Sin cierre de compra ni datos de retail local latinoamericano |
| DespensaIA (español) | Foto del ticket, la IA parsea y llena la despensa; recetas y comunidad. Economía de tokens diarios gratis, con más tokens por ver anuncios | Enfocada a España. El modelo de tokens delata que el costo de modelo por usuario no cierra |
| Fango | Ticket primero: fotografía el recibo y la IA escribe por ti. Hogar compartido hasta cuatro personas | Solo rastrea. Sin recetas fuertes ni ciclo de compra |
| ConsumeSmart | Ticket como registro de máxima fidelidad de lo que entró a la casa | Igual: entrada resuelta, salida no |
| Eatvora | Recetas con lo que vence, Pantry Health Score, plan semanal, nutrición, hogar compartido, gratis | Genérica; sin ancla local ni cierre de compra |
| Pantryfy | Único que declara un agente de IA que corre el ciclo semanal de planificación solo | Sin inventario auditable ni datos locales |
| ChefsPantry | Códigos, ticket y manual; la caducidad alimenta directamente el motor de planificación | Sin voz como vía principal |
| Recipy | Cámara, ticket, avisos de caducidad, recetas y sincronización multiplataforma en capa gratis | Amplia y superficial |
| MealThinker | Conversacional puro: el inventario se mantiene hablando, sin pantalla aparte | USD 15 al mes, sin lector de códigos y sin fechas de caducidad como sistema |

### 4.2 Los de antes

| Quién | Qué hace | Dónde está flojo |
|---|---|---|
| Pantry Check | Lector de códigos muy rápido, ubicaciones, avisos, lista sugerida | Solo iOS; tope de ~200 ítems en el plan gratis; todo entra escaneando |
| NoWaste | Caducidad primero, iOS y Android, hace visible el costo de tirar | Sin recetas ni planificación; registro manual |
| Fridgely | Códigos de barras y recordatorios, gratis | Muy básico |
| Grocy | Inventario completo con caducidad, autoalojado | Para entusiastas; nada de IA |
| Kitche | Importa la compra desde la cuenta de fidelidad del supermercado | Atado al retail británico. La idea es excelente y sigue sin copiarse en LatAm |
| SuperCook / Samsung Food | Recetas a partir de lo que tienes | No sostienen inventario ni caducidad |
| Samsung Bespoke AI Family Hub | Cámara interna con AI Vision y Gemini, anunciado en CES 2026. Reconoce 37 frescos y hasta 50 empaquetados pre-registrados por el usuario | Requiere comprar la nevera. El techo de reconocimiento es estrecho para una despensa real |
| Winnow, Orbisk, Leanpath, Kitro | Merma en cocina con cámara y balanza; ~800 ingredientes con ~90% de acierto | Precio por cotización, venta empresarial, nada para el hogar |
| MarketMan, Apicbase | Costo de alimentos, inventario teórico contra real, recetas y proveedores multi-sede. MarketMan publica USD 199 al mes | Sin FEFO por lote con etiqueta ni bitácora de temperatura; sin producto en español para América Latina |
| Xenia, SwiftSensors, SmartSense | Bitácoras de temperatura HACCP con sensores | Cumplimiento sí, inventario y menú no |
| MOCREO, YoLink | Sensores de nevera con alerta de corte de luz y hora exacta de caída y retorno | No hablan con ninguna app de inventario. Nadie cruza la excursión térmica con la lista de productos afectados |

### 4.3 Qué se cayó como diferencial

Tres cosas que este documento daba por disponibles ya no lo están:

- **"Cociné esto" como descarga de inventario.** Era el hallazgo central del veredicto. Pantry
  Persona lo vende con esa frase textual y Despify lo tiene como Cooked Mode. Sigue siendo
  obligatorio construirlo, pero ya no diferencia.
- **"En español".** Despify y DespensaIA son nativas en español. Lo que sigue libre es
  específicamente América Latina: ticket mexicano y colombiano, marcas propias de cadenas locales,
  diccionario de productos por país. España no es LatAm y esas dos apuntan a España.
- **"Recetas con IA según lo que tienes".** Ya estaba descartado. Se confirma, y ahora también lo
  hacen los asistentes de propósito general con memoria.

### 4.4 Qué sigue siendo hueco

- **Frontera determinista declarada.** Toda la oleada de 2026 es IA de punta a punta. Ninguna
  declara que las fechas, las cantidades, las alergias y el dinero los decide un sistema
  determinista y no una inferencia. Es argumento de confianza y, en alérgenos, de seguridad. Es el
  diferencial más fuerte y el más barato de sostener.
- **Cierre de la compra en América Latina.** Instacart resolvió esto en Estados Unidos: su
  Developer Platform da acceso a más de 85 000 comercios y paga comisión de afiliado vía Impact, y
  ya corre con NYT Cooking y con la app de electrodomésticos de GE. En América Latina no hay
  equivalente. El portal de Rappi Partners es para que comercios *reciban* pedidos por OAuth, no
  para que una app de terceros *ponga* un carrito. Esto bloquea el momento de negocio de la demo
  tal como está planteado, y el bloqueo es comercial, no técnico.
- **Ticket latinoamericano.** Todos los OCR de la oleada están entrenados en tickets de Estados
  Unidos, Reino Unido y España.
- **Temperatura y cortes de luz.** El hardware ya existe y avisa con hora exacta de caída y de
  retorno de la corriente. Ninguna app de inventario lo consume. El aviso de "tu nevera estuvo a
  12 °C durante tres horas: revisa estos seis productos" sigue sin darlo nadie.
- **Importación desde programas de fidelidad locales**, al estilo Kitche.
- **B2B de 3 a 20 sedes en América Latina**, con el matiz de precio de la sección 2.

### 4.5 Lo que dice la forma del mercado

Media docena de estas apps publican comparativas de sus competidoras en sus propios blogs y compiten
por posicionamiento orgánico con la misma consulta. Eso no es un mercado maduro: es un mercado
saturado de productos indie con barrera de entrada casi nula. Confirma el diagnóstico original —el
riesgo es de retención y distribución, no técnico— y agrega uno: cualquier feature de este producto,
salvo la frontera determinista y el cierre de compra local, la reproduce alguien en un fin de
semana.

## 5. Hardware

Recomendación de fondo: versión 1 sin hardware. El hardware entra después como accesorio opcional y
como producto vendible en B2B.

| Hardware | Costo aproximado | Qué habilita | Cuándo |
|---|---|---|---|
| Sensor BLE de temperatura y humedad | USD 10–25 | Vida útil real; alerta por corte de luz o puerta abierta | v2, alto retorno |
| Etiquetas NFC o QR para recipientes | USD 0,30–1 cada una | Sobras en un toque | v2, barato |
| Impresora térmica Bluetooth de etiquetas | USD 40–120 | Etiqueta FEFO con producto, fecha, hora y responsable | B2B, vendible ya |
| Báscula Bluetooth de cocina | USD 20–60 | Cantidades reales; peso de merma | Opcional |
| Sensor magnético de puerta | USD 10–20 | Uso real de la nevera | Marginal |
| Red de sondas con concentrador | USD 300–1 500 por sede | Bitácora HACCP continua y a prueba de manipulación | B2B, es el ingreso |
| Cámara dentro de la nevera | USD 30–80 | Inventario automático | No hacerlo |

La cámara interna implica condensación, oclusión, iluminación y alimentación eléctrica: es un
proyecto de hardware completo y es el terreno donde Samsung juega con escala.

El sensor de temperatura es el único accesorio que convierte una promesa en un hecho. No conviene
fabricar nada: certificar dos modelos comerciales como compatibles y leerlos por Bluetooth da el 90%
del beneficio sin inventario ni soporte de fabricación.

Versión honesta sin sensor: estimar con tablas públicas (FoodKeeper de la FDA, USDA) más la zona de
guardado, siempre que el texto diga "estimado".

| Alimento | Refrigerado a 4 °C | Después de abrir |
|---|---|---|
| Pollo o carne molida cruda | 1–2 días | — |
| Leche | Hasta la fecha impresa | 5–7 días |
| Huevos con cáscara | 3–5 semanas | — |
| Espinaca y hojas verdes | 3–5 días | 2–3 días |
| Zanahoria | 3–4 semanas | — |
| Queso duro | 6 meses | 3–4 semanas |
| Sobras cocidas | 3–4 días | — |

La diferencia entre columnas es justo lo que la idea original no capturaba: el momento de apertura.

## 6. Cómo vendérselo a un cliente

- **A una familia: dinero, no sostenibilidad.** "Tu casa tira cerca de X al mes en comida. Toma tres
  fotos de tus tickets y te decimos qué cocinar esta semana para no tirarla." La sostenibilidad va
  como razón secundaria.
- **A un restaurante: costo de alimentos e inspección.** No se vende "menos desperdicio", se vende
  punto porcentual de costo de alimentos y estar listo para la visita sanitaria. Las bitácoras
  electrónicas se aceptan en los 50 estados de Estados Unidos y los inspectores confían más en ellas
  que en el papel. Posición: una décima parte del precio de un sistema de cámara, con el teléfono que
  los cocineros ya tienen.
- **A un hotel: buffet y multi-sede.** Pronóstico de buffet, control de minibar y una sola bitácora
  consolidada de temperaturas. El comprador es operaciones.
- **A un inversionista: cuña y foso.** Problema medido, cuña defendible en español y retail
  latinoamericano, expansión hacia un mercado que ya paga. El foso es el grafo de productos, tickets
  y vida útil por país.

Canales que valen más que la publicidad: cadenas de retail (quieren datos de canasta y recompra),
fabricantes de electrodomésticos (quieren software que diferencie sus neveras) y aseguradoras o
servicios públicos (la alerta de corte de frío se lee como prevención de pérdidas).

## 7. Features no mencionadas que valen la pena

- Registro de desperdicio con dinero. Si solo se agrega una, es esta.
- "Cociné esto" para descontar inventario de un toque.
- Sobras y comida preparada como categoría propia, con caducidad automática.
- Alerta de excursión térmica por corte de luz o puerta abierta (requiere sensor).
- Modo congelador con fecha de congelación y "úsalo antes de".
- Plan semanal de comidas armado desde lo que vence.
- Presupuesto semanal y comparación de precios entre tiendas.
- Roles del hogar: quien va al súper recibe la lista; quien cocina recibe qué usar.
- Lista por WhatsApp, compartible al grupo de la casa.
- Base de productos colaborativa, sembrada desde Open Food Facts.
- Donar o regalar excedente a vecinos.
- Funcionamiento sin conexión y en Android de gama baja.

## 8. Límites legales por región

El detonante de casi todo es el tratamiento de datos de salud. Sin ellos, esto es una app de cocina
y el panorama regulatorio se vuelve ordinario.

| Región | Qué aplica | Consecuencia práctica |
|---|---|---|
| Estados Unidos | Sin ley federal; mosaico estatal (CCPA/CPRA y ~20 estados). Leyes de datos de salud del consumidor, con My Health My Data de Washington y su derecho privado de acción. Regla de notificación de brechas de la FTC para apps de salud. COPPA si hay menores. | Las inferencias sobre dieta y condiciones pueden contar como datos de salud del consumidor. Consentimiento por finalidad; no vender ni compartir. |
| Unión Europea | RGPD art. 9: salud es categoría especial. Ley de IA art. 50, transparencia desde el 2 de agosto de 2026, multas hasta 15 M EUR o 3% de facturación. MDR anexo VIII regla 11. | Hay que informar que se interactúa con IA. El software de asesoría nutricional presentado para gestionar una enfermedad cae en clase IIa; presentado como bienestar general, queda fuera. |
| México | Nueva LFPDPPP de marzo de 2025: penas penales, tribunales especializados, multas duplicadas para datos sensibles. NOM-051 de etiquetado frontal. COFEPRIS para claims de salud. | Consentimiento expreso y medidas técnicas demostrables. Los sellos NOM-051 son además un dato aprovechable. |
| Colombia | Ley 1581 de 2012: datos sensibles solo con autorización explícita; registro de bases ante la SIC; proyecto de reforma de agosto de 2025 que endurece sanciones. | Autorización explícita, separada y documentada. El marco se endurecerá durante la vida del producto. |
| Resto de América | Brasil con LGPD y ANPD activa; Chile con la ley 21.719 y su nueva agencia; Argentina con la 25.326 y reforma pendiente. | Convergen al modelo europeo. Diseñar al estándar RGPD y el resto sale casi gratis. |
| Si se entra a B2B | Código de Alimentos de la FDA (frío a 41 °F / 5 °C con registro), FSMA 204 con cumplimiento corrido al 20 de julio de 2028, HACCP en la UE. | No es un obstáculo: es el argumento de venta, porque el cumplimiento es la partida presupuestal que sí se aprueba. |

Tres reglas de diseño que ahorran casi todo lo anterior:

1. Los datos de salud son opcionales y separables; la app funciona completa sin ellos.
2. Nunca se emite un juicio de inocuidad: "estimado", "revisa la etiqueta", y la decisión es del
   usuario.
3. Se declara siempre que hay IA de por medio, y el filtro de alérgenos se prueba con casos
   dedicados.

## 9. Lo que no se preguntó y conviene mirar

- La métrica que importa no es usuarios activos, es exactitud del inventario al día 30.
- Prueba de conserje antes de construir: diez familias, dos semanas, notas de voz a un número de
  WhatsApp y una persona del equipo registrando a mano.
- La prueba comercial que se necesita es "reducimos el desperdicio medido un X% en ocho semanas".
- Techo de costo por usuario desde el día uno.
- El nombre: revisar registro y dominio, y considerar que "freez" ancla al congelador cuando el
  producto habla de la nevera y de la compra.
- El equipo necesita alguien de datos de alimentos: vida útil, alérgenos, equivalencias.
- Riesgo de plataforma: Samsung y Google pueden empaquetar esto en el electrodoméstico. Su alcance
  son neveras de gama alta, no teléfonos, pero la ventana no es infinita.
- Riesgo de plataforma por el otro lado: Pantry Persona vive dentro de ChatGPT y de Claude. Si el
  hogar ya conversa con un asistente, la despensa puede terminar siendo una memoria del asistente y
  no una app. Conviene decidir pronto si este producto también quiere estar ahí.
- La ventana de la oleada indie: una decena de apps lanzadas en 2025 y 2026 pelean el mismo término
  de búsqueda. Casi ninguna tiene retención probada. Es probable que la mayoría cierre, y también
  que alguna capture la categoría antes de que este producto salga.
- Alianzas que aceleran: Open Food Facts, programas de fidelidad de retail, fabricantes de neveras.

## Fuentes

- EPA, *Estimating the Cost of Food Waste to American Consumers* (abril de 2025).
- Comparativas de apps de despensa 2026 (Fango, Recipy, ChefsPantry, Pantryfy, Eatvora,
  Pantry Persona, MealThinker), consultadas el 9 de septiembre de 2026.
- Pantry Persona: página de preguntas frecuentes y planes (gratis y Pro a USD 7,99 al mes).
- Despify: página de características y notas de la versión 2.5. DespensaIA: sitio y ficha de
  Google Play.
- Orbisk, sistemas de gestión de merma 2026 y guía de software de costo de alimentos; Winnow,
  precios y planes; MarketMan, precio publicado; Apicbase, cotización multi-sede.
- Samsung Newsroom: AI Vision con Gemini (CES 2026) y actualización de Family Hub (mayo de 2026).
- Instacart: anuncio del Developer Platform, documentación de conversiones y pagos de afiliado, y
  cobertura de Grocery Dive sobre las integraciones con NYT Cooking y GE Appliances.
- Uber Developers, flujos de activación de integración; perfil público de la API de Rappi y portal
  de Rappi Partners México.
- Fichas de producto de MOCREO y YoLink para sensores de nevera con alerta de corte de luz.
- NAMSA, clasificación de software como dispositivo médico bajo MDR.
- Ley de IA de la Unión Europea, art. 50.
- LFPDPPP de México (2025); Ley 1581 de 2012 de Colombia.
- Federal Register, extensión de la fecha de cumplimiento de FSMA 204.
- Guías de monitoreo de temperatura y HACCP en restaurantes, 2026.

Panorama regulatorio para orientar decisiones de producto, no asesoría legal. Antes de lanzar en
cada mercado, y sobre todo antes de recolectar cualquier dato de salud, se requiere revisión con
abogado local.
