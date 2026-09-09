# Integraciones de compra (FE5)

Fecha: 4 de septiembre de 2026. Estado de plataformas y programas verificado en esa fecha; cambia
rápido y conviene reconfirmar antes de comprometerse.

## En una frase

La plataforma de domicilio no vende una puerta de entrada para que otra app le traiga pedidos: vende
una vitrina para que los comercios le vendan a *sus* usuarios. Freezai no es ni comercio ni punto de
venta, así que no hay una figura en la que encaje. Lo que se puede construir hoy no es la
integración: es el atajo que le ahorra al usuario retipear la lista, que cubre el 90% del beneficio
percibido con el 2% del trabajo.

El objetivo no se descarta. El modelo existe y funciona: Instacart y Kroger lo operan hoy. Solo no
existe todavía en Latinoamérica.

## Los diez aspectos de la limitante

1. **Las APIs son del lado de la oferta, no del comprador.** Uber Eats expone su familia de APIs por
   el portal de desarrolladores para restaurantes, plataformas de marketplace, proveedores de punto
   de venta y socios de logística: gestionar tiendas, menús y pedidos. Rappi igual: catálogo,
   disponibilidad de tienda, ciclo de vida del pedido, conciliación financiera y webhooks. Ninguna
   operación dice "arma este carrito y cóbrale a este usuario final".
2. **El acceso no es auto-servicio.** El portal de socios de Rappi entrega credenciales OAuth 2.0
   solo después de que un contacto comercial aprueba el ingreso; luego dan ambiente de desarrollo y
   después una ruta a producción.
3. **Asimetría de negociación.** Aprueban integraciones que les traen volumen o les resuelven un
   problema propio. Una app con quinientos usuarios no es ninguna de las dos cosas.
4. **El catálogo de supermercado no es estable.** El surtido de Rappi Súper y Turbo varía por ciudad
   y por tienda oscura, y el precio y la disponibilidad cambian dentro del mismo día. Mapear "leche
   entera 1 L" al identificador correcto en cada ciudad es mantenimiento permanente.
5. **Los reemplazos corrompen el inventario.** En compra de mercado el repartidor sustituye lo que no
   hay. Justo la feature que promete precisión introduce el error que la destruye.
6. **Pago y responsabilidad quedan en nombre propio.** Si el pedido sale de la app, hay que definir
   quién cobra, quién responde por faltantes y quién reembolsa. Se absorbe un flujo de soporte que no
   se controla, sobre un pedido que no se ejecuta.
7. **La economía apunta al afiliado, no a la API.** Si la monetización es comisión por canasta, lo que
   se necesita es un enlace de referido que pague por pedido. La API de comercio no paga nada y
   cuesta integración y mantenimiento.
8. **Automatizar la app del usuario no es una opción.** Scraping o automatización de la sesión viola
   los términos de servicio, se rompe con cada actualización de la app ajena y, en la Unión Europea,
   el catálogo está protegido además por el derecho *sui generis* de bases de datos.
9. **Cada país es una negociación distinta.** Rappi en Latinoamérica, Uber Eats multi-país, DiDi Food
   en México, Instacart en Estados Unidos, y Cornershop absorbido por Uber. Cinco integraciones,
   cinco contratos, cinco calendarios.
10. **El camino real hacia la integración es comercial.** Juntar usuarios con el enlace profundo,
    medir cuántas canastas se generan y con qué valor, y presentarse como generador de demanda con
    datos de canasta. Alternativa que suele abrir antes: hablar con el retailer directo, que quiere
    recompra y datos, más que con el intermediario de reparto.

## La escalera de opciones reales

| Peldaño | Qué es | Qué hace falta | Dónde sirve |
|---|---|---|---|
| 0, hoy | Enlace profundo por ítem, lista al portapapeles, envío por WhatsApp al grupo de la casa o al tendero | Nada, ningún permiso de terceros | Todos los países |
| 1, hoy | Programa de afiliados. Uber tiene programa público que paga comisión por cada usuario que hace su primer pedido, negociable según país y audiencia | Registro en el programa; no requiere API | Donde Uber opera. En Rappi hay que preguntar: no se encontró programa público documentado |
| 2, hoy en EEUU | Carrito real donde ya hay API abierta. La Developer Platform de Instacart es auto-servicio desde el 20 de julio de 2026: se crea la llave en el panel, se llama al endpoint que genera una página de lista o receta, y el usuario abre el enlace, elige tienda, agrega productos y paga. Kroger tiene una Cart API pública que agrega ítems al carrito del usuario con autorización OAuth2 y PKCE | Cuenta de desarrollador | Estados Unidos. Es la prueba de que el modelo funciona |
| 3, mediano | Middleware de receta a carrito. Chicory tiene integración directa con más de 70 retailers y en 2026 sumó Albertsons y 15 de sus banners; Northfork opera el caso de Walmart; Samsung Food ofrece lo suyo | Acuerdo con el middleware, no con cada retailer | EEUU y Europa. Es también la lista de posibles socios o compradores |
| 4, mediano, LatAm | Retailer directo: Éxito, Cencosud, Soriana, Chedraui. Sin API pública, se abre por acuerdo comercial | Usuarios en sus ciudades y una propuesta de recompra. La moneda es dato de canasta | La vía más corta en Latinoamérica |
| 5, con volumen | Programa de socios de Rappi o Uber, con carrito armado de verdad | Canastas medibles y una conversación comercial | El objetivo original de FE5, al final y no al principio |

Los peldaños 0 a 3 no dependen de aprobación de terceros. El 4 y el 5 son ventas, no ingeniería.

## Catálogo de plataformas donde se puede comprar el ingrediente que falta

Modelo de acceso: **carrito** significa que existe una vía técnica para armarlo; **afiliado**, que
paga comisión por enlace; **enlace**, que solo se puede abrir con búsqueda precargada; **acuerdo**,
que hace falta una conversación comercial.

### Latinoamérica

| Plataforma | Región | Qué es | Acceso real |
|---|---|---|---|
| Rappi · Rappi Turbo | 9 países; Turbo en 7 | Súper, farmacia, licores; +200 000 comercios en +300 ciudades | Enlace · portal de socios solo del lado del comercio, con aprobación comercial |
| PedidosYa · PedidosYa Market | Andina y Cono Sur | Quick commerce y supermercado, +12 000 comercios | Enlace · lado comercio |
| Uber Eats (incluye lo que fue Cornershop) | Multi-país | Restaurantes y mercado en la misma app | Afiliado · programa público que paga por primer pedido |
| iFood | Brasil | Dominante en su mercado | Enlace · lado comercio |
| DiDi Food | México y otros | Comida y conveniencia | Enlace |
| Éxito · Carulla | Colombia | Retailer con app propia y Puntos Colombia | Acuerdo · sin API pública, pero es la puerta más corta |
| Jumbo · Metro (Cencosud) | Colombia, Chile, Argentina, Perú | Retailer regional | Acuerdo |
| Soriana · Chedraui · La Comer | México | Cadenas con comercio electrónico propio | Acuerdo |
| Walmart México | México | La red de mercado más grande del país | Acuerdo · su API transaccional requiere aprobación especial |
| Jüsto | México | Supermercado nativo digital | Acuerdo · por tamaño, más abordable que una cadena tradicional |
| Tottus, Wong, Plaza Vea | Perú, Chile | Retailer con app propia | Acuerdo |
| **Tienda de barrio por WhatsApp** | Toda la región | Donde de verdad se compra buena parte del mercado diario | **Carrito** · se manda la lista al chat del tendero. Sin permisos ni API, funciona hoy |

### Estados Unidos

| Plataforma | Qué es | Acceso real |
|---|---|---|
| Instacart | Agregador de cientos de cadenas | **Carrito** · plataforma de desarrolladores auto-servicio desde julio de 2026 |
| Kroger | Segunda cadena de alimentos del país | **Carrito** · Cart API pública con autorización OAuth2 del usuario |
| Walmart EEUU | La cadena más grande | Afiliado · la API de afiliados es de solo lectura; la transaccional exige aprobación especial y plan de negocio revisado |
| Amazon Fresh · Whole Foods | Mercado de Amazon | Afiliado · sin API de carrito para terceros |
| Target · Shipt, Albertsons, HEB, Publix, Wegmans | Cadenas regionales fuertes | Acuerdo, o vía middleware que ya las tiene integradas |

### Middleware de lista y receta a carrito

| Plataforma | Región | Qué es | Acceso real |
|---|---|---|---|
| Chicory | EEUU | Botón de ingredientes con integración directa a +70 retailers; en 2026 sumó Albertsons y 15 banners | Acuerdo · un contrato y se heredan decenas de tiendas |
| Northfork | EEUU y Europa | Tecnología de receta comprable; opera el caso de Walmart | Acuerdo |
| Samsung Food (antes Whisk) | Global | Recetas comprables dentro de un ecosistema mayor | Acuerdo · y también competidor |
| Smart Commerce y similares | EEUU y Europa | Intermediarios de "comprar ahora" para marcas | Acuerdo |

### Europa

| Plataforma | Qué es | Acceso real |
|---|---|---|
| Tesco, Sainsbury's, Ocado, Waitrose, ASDA, Morrisons | Retailer con cuenta de fidelidad | Acuerdo · Kitche demostró que por ahí se importa la compra |
| Carrefour, Rewe, Albert Heijn, Picnic, Mercadona | Retailer con comercio electrónico propio | Acuerdo |
| Glovo, Wolt, Bolt Food | Reparto con mercado y conveniencia | Enlace · lado comercio |

De todo el catálogo, solo tres filas dicen "carrito" y una de ellas es WhatsApp. Eso resume el tamaño
real de la oportunidad y por dónde empezar.

## Cerrar el ciclo sin API

Armar el carrito es la mitad del problema. La otra mitad es que la compra vuelva al inventario, y
ninguna plataforma devuelve las líneas del pedido sin acuerdo. Tres formas de resolverlo hoy:

- **El usuario comparte el correo de confirmación** con la hoja de compartir del teléfono, o lo
  reenvía a una dirección tipo `compras@freezai`. Cero permisos, cero integración, y llega con los
  reemplazos ya aplicados, que es justo lo que la confirmación inicial no tiene.
- **Acceso al buzón con consentimiento** (API de Gmail). Funciona, pero el permiso es de categoría
  restringida y exige una evaluación de seguridad anual por un tercero certificado, con costo de
  miles de dólares al año. Real, pero no para la versión 1.
- **Foto de la pantalla del pedido**, con el mismo OCR de los tickets físicos. La ruta más barata y
  sin dependencias externas.

## Bloqueos que pueden hacerla imposible o muy poco viable

| Bloqueo | Por qué | Tipo |
|---|---|---|
| No hay OAuth de consumidor en Rappi ni Uber Eats | Sin un permiso que diga "actuar sobre el carrito de este usuario final", ninguna cantidad de ingeniería lo resuelve. No es una limitación técnica: la figura no existe | Duro · solo se levanta por contrato |
| Si se cobra en la app, se pasa a ser comercio de registro | Pasarela, KYC, cumplimiento PCI DSS, contracargos y factura electrónica por país (CFDI en México, facturación DIAN en Colombia). Convierte una feature en una empresa de pagos | Duro · económico |
| No devuelven los datos del pedido | El más grave para este producto: sin líneas del pedido ni sustituciones, la compra no entra al inventario y la feature no cierra el ciclo. Se mitiga con el correo de confirmación, no con la API | Funcional |
| Precio y disponibilidad que no se controlan | Mostrar un precio que después no se cumple es materia de protección al consumidor: Profeco en México, SIC en Colombia. Si no se tiene el precio por contrato, no se muestra | Legal · evitable |
| Categorías restringidas por edad | Alcohol y farmacia exigen verificación de edad que un tercero no puede asumir por la plataforma | Parcial · excluye categorías |
| Automatizar la sesión del usuario o raspar el catálogo | Viola términos de servicio, se rompe con cada actualización, y en la UE choca con el derecho *sui generis* de bases de datos | Duro · esa vía queda cerrada |
| Uso de marca y logo | Poner la marca de Rappi en la interfaz va más allá del uso nominativo tolerado sin autorización | Menor · se resuelve con texto neutro |
| Surtido de tienda oscura | La canasta semanal de una familia muchas veces no es surtible por Turbo o equivalente | De utilidad |
| La economía del usuario | Tarifa de domicilio más sobreprecio contra un mercado presencial más barato. En muchos hogares la integración no se usaría aunque existiera | De demanda · el que hay que medir primero |
| Fragmentación por país y plataforma | Cada combinación es un contrato distinto y nada se reutiliza, salvo el mapeo propio de productos | De escala |

Un miedo que no aplica: las reglas de compra dentro de la app no cubren bienes físicos, así que
enlazar hacia afuera para comprar mercado está permitido en iOS y Android.

## Cómo se decide

Lanzar el peldaño 0 y medir una sola cosa: qué porcentaje de listas termina en un enlace abierto
hacia una plataforma de compra.

- Por debajo del 10%: la integración profunda no cambiaría nada y la discusión se cierra sola.
- Por encima del 30%: es exactamente el número que abre la conversación comercial con Rappi, con un
  retailer o con un middleware. Y en esa conversación ya no se pide acceso: se lleva demanda.

## Cómo abordarlo en una demo con un cliente

El cliente que pregunta por Rappi no está pidiendo una integración: está pidiendo ver que la compra
se resuelve sin retipear. Eso se demuestra hoy, en su teléfono, sin depender de nadie. La regla es
demostrar lo real y ser explícito sobre lo que falta, porque un flujo presentado como integrado
cuando no lo está es lo que hunde la credibilidad en la segunda reunión.

### Guion de tres minutos

| Tiempo | Qué se muestra |
|---|---|
| 0:00 | La lista viva ya armada, con faltantes reales. Si se consiguen dos tickets del cliente antes de la reunión, la demo corre con sus propios datos y vale diez veces más |
| 0:40 | Botón de comprar: hoja con las opciones reales — abrir en la app de domicilio, mandar por WhatsApp al tendero, copiar la lista |
| 1:00 | Se elige la app de domicilio y se abre con el producto ya buscado. Se agrega allí y se vuelve a Freezai, donde el ítem queda como pendiente de confirmar |
| 1:40 | Se comparte el correo de confirmación del pedido y los ítems entran al inventario con su fecha estimada. Aquí se ve el ciclo cerrado, que es lo que ninguna app de la competencia muestra |
| 2:10 | Segundo dispositivo o grabación: el flujo completo de carrito armado por API, hecho con Instacart. Sirve para decir "así se ve cuando la plataforma tiene programa abierto, y el camino existe" |
| 2:40 | Cierre con la métrica: se mide qué porcentaje de listas termina en compra, y ese número es el que abre la conversación con Rappi |

### Respuestas a las tres preguntas que siempre llegan

- **"¿Está integrado con Rappi?"** — "Salimos hacia Rappi con la compra pre-armada. El carrito armado
  dentro de Rappi requiere su programa de socios, que se abre por volumen. En Estados Unidos el flujo
  completo ya lo hacemos con Instacart, que tiene plataforma abierta."
- **"¿Cuándo estaría?"** — "No lo prometemos por fecha, porque no depende de nosotros: depende del
  volumen que llevemos a la mesa. Lo que sí prometemos es la métrica que lo desbloquea."
- **"¿Y si nunca abren?"** — "El 90% del beneficio para el usuario no depende de ellos y ya está en la
  versión 1. Y en esta región la puerta más corta no es el repartidor, es el retailer."

### Qué no hacer en la demo

- **No automatizar la app ajena en escena.** Scraping o automatización de la sesión viola términos, se
  rompe con cualquier actualización y un cliente técnico lo detecta.
- **No mostrar precios de la plataforma.** Sin acuerdo no hay derecho a esos datos, y un precio que no
  se cumple es materia de protección al consumidor.
- **No usar el logo ni la marca.** La pantalla dice "tu app de domicilio", no el nombre ajeno. Además
  de ser lo correcto legalmente, evita que la demo parezca una alianza que no existe.
- **No etiquetar como "integrado" un flujo simulado.** Si hace falta ilustrar el flujo completo con
  pantallas de maqueta, la etiqueta "flujo ilustrativo, no integrado" va visible en la pantalla.

### La jugada comercial detrás de la pregunta

Quien pregunta por Rappi suele ser quien puede abrir una puerta. Conviene invertir la carga:

- Si el cliente es un **retailer**, la propuesta es "te integramos a ti antes que a Rappi", porque lo
  que él gana es recompra y datos de canasta.
- Si es un **inversionista**, la respuesta es la métrica: por encima del 30% de listas convertidas, la
  integración deja de ser una petición y pasa a ser una negociación.
- Si es un **cliente corporativo** que quiere la integración, la vía es que firme intención de uso: con
  ese volumen documentado se pide la reunión de partnerships, y no antes.

## Cómo dejarlo por escrito sin comprometerse

Si la instrucción es que Rappi y Uber Eats aparezcan en la propuesta, aparecen. La forma de hacerlo
sin quedar expuesto es **incluir la condición dentro de la misma frase**, no en una nota al pie ni en
una conversación posterior. Así, el día en que haya que decir que el carrito no va, no es un
retroceso: es lo que el documento decía desde el principio.

No es lo mismo decir "integración con Rappi" que decir "salida hacia Rappi desde la lista de
compras; el carrito armado dentro de Rappi depende de su programa de socios". La segunda frase ya
contiene el motivo, y quien la leyó no puede sentirse sorprendido después.

### Texto listo para la propuesta

> **Compra del faltante.** Desde la lista de compras, Freezai lleva al usuario a la plataforma donde
> quiera comprar — Rappi, PedidosYa, Uber Eats, el supermercado o el tendero del barrio por
> WhatsApp — con los productos ya identificados, y la compra regresa al inventario a partir del
> comprobante. El carrito armado automáticamente dentro de cada plataforma depende del programa de
> socios de cada una, que se habilita por volumen de pedidos generados; el diseño contempla esa
> integración y no la requiere para funcionar.

Tres cosas hace ese párrafo a la vez: nombra Rappi y Uber Eats, describe algo que ya funciona hoy, y
deja registrada la dependencia externa. Es el mismo contenido que exige el jefe, con el seguro
puesto.

### En la tabla de alcance

Se lista como fase con dependencia, nunca con fecha:

| Fase | Alcance | Depende de |
|---|---|---|
| v1 | Salida a la plataforma con productos identificados; retorno por comprobante | Nada |
| Futuro | Carrito armado dentro de la plataforma | Programa de socios de cada plataforma, habilitado por volumen |

Una fecha convierte una expectativa en un compromiso. Una dependencia declarada mantiene la
expectativa y traslada la causa a donde de verdad está.

### Lo único que no conviene hacer

Presentarlo como integración existente. Ese es el escenario en que "luego decimos que no puede ir"
sí duele: el cliente ya tomó decisiones con esa información, y el equipo pierde credibilidad en todo
lo demás que dijo, incluso en lo que era cierto. El objetivo del jefe — que Rappi aparezca y sostenga
la conversación — se cumple igual con el párrafo de arriba, sin esa factura.

### Bullet listo para "pasos posteriores"

> **A futuro — compra dentro de la plataforma.** Habilitar el carrito armado en Rappi, Uber Eats y
> otras plataformas de domicilio, sujeto al programa de socios de cada una. En la versión 1 la compra
> ya sale hacia esas apps con los productos identificados y regresa al inventario por comprobante.

Cuidado con el verbo: "implementar en Rappi" suena a que depende del equipo, y si después no ocurre,
la culpa queda de este lado. **Habilitar**, **sumar** o **abrir**, siempre con "sujeto al programa de
socios", nombran la dependencia sin sonar a excusa.

Dos frases para tener listas en la reunión:

- *"¿Eso está?"* — "Está la salida hacia la plataforma; el carrito dentro de ella depende de su
  programa de socios."
- *"¿Cuándo?"* — "No lo comprometemos por fecha porque no depende de nosotros: depende del volumen de
  pedidos que generemos."
