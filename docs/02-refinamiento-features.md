# Refinamiento feature por feature

Fecha: 4 de septiembre de 2026. Incorpora las decisiones tomadas en revisión: la captura por voz se
queda, las recetas se enlazan en vez de copiarse, y el plan de alimentación entra como preferencia
declarada por el usuario.

Convención: **Deja** lo que se mantiene tal cual, **Quita** lo que sale, **Cambia** lo que se
sustituye por otra cosa, **Agrega** lo que no estaba.

## Captura de datos

Es la decisión más fuerte del planteamiento original. Solo hay que invertir el orden de importancia.

- **Deja** — La captura por voz se queda, sin condiciones. Grabar voz no es por sí solo un dato
  sensible y no hay obstáculo legal que obligue a quitarla. Lo que hay son cuatro reglas de manejo.
- **Deja** — Entrada manual escondida como fallback, sin promoverla.
- **Cambia** — El ticket pasa a ser la vía principal y la voz la excepción. Una foto carga treinta
  ítems; una nota de voz carga tres. La voz gana al guardar la compra ítem por ítem o al registrar
  sobras, no en la carga masiva.
- **Agrega** — Confirmación en un paso tras el OCR: el ticket entra como borrador editable, no como
  verdad. Ahí se corrigen cantidades y se aprende el diccionario de la cadena.
- **Agrega** — Las cuatro reglas: (1) nunca generar huella vocal ni usar la voz para identificar a
  nadie; (2) borrar el audio tras transcribir, con opción de conservarlo unos días para corregir
  errores, como minimización voluntaria y no como obligación; (3) consentimiento aparte y revocable
  si algún día se entrena un modelo con esas grabaciones; (4) sin audio en perfiles de menores.
- **Quita** — Conservar la imagen del ticket más allá de lo necesario para procesarla: la foto lleva
  nombre, dirección y los últimos dígitos de la tarjeta. El dato extraído se queda; la imagen no.

### Por qué WhatsApp puede grabar voz, y nosotros también

Grabar la voz de alguien no es tratar un dato biométrico. El RGPD llama biométrico al dato que
resulta de un tratamiento técnico específico que permite identificar de forma única a una persona,
es decir, la huella vocal que reconoce quién habla. Una nota de voz que se transcribe para saber que
entraron dos litros de leche es contenido, no huella. La distinción es la misma que entre una foto
de un plato y un reconocimiento facial.

WhatsApp graba porque el usuario aprieta un botón para enviar un mensaje: la grabación es el
servicio, y la base legal es la ejecución del contrato. Nuestro caso es idéntico. No se necesita
consentimiento especial de datos sensibles; se necesita el permiso de micrófono del sistema,
declararlo en el aviso de privacidad y no hacer con el audio nada que el usuario no espere.

Los castigos del sector no fueron por grabar:

| Caso | Qué salió mal | Lección aplicable |
|---|---|---|
| Siri y Google Assistant, 2019 | Contratistas humanos escuchando grabaciones sin que estuviera claramente informado | Si una persona va a oír audio, hay que decirlo y pedirlo aparte |
| Alexa, FTC 2023 | Retención indefinida de grabaciones de niños; multa de USD 25 millones bajo COPPA | Retención con plazo, borrado real cuando se pide, nada de audio de menores |
| Asistentes en general | Escucha continua sin activación explícita | Grabar solo mientras el usuario mantiene el botón |

## FE1 · Caducidad y prioridad de consumo

Es el corazón del producto. Le falta una pieza de información y le sobra una promesa.

- **Deja** — Fecha de vencimiento por ítem, estimación de vida útil para frescos sin fecha, y el
  orden FEFO: lo que vence primero se usa primero.
- **Agrega** — Fecha de apertura del envase. Sin esto el estimado engaña más que la fecha impresa:
  leche cerrada dura semanas, abierta cinco días; queso duro seis meses cerrado, tres o cuatro
  semanas abierto.
- **Agrega** — Zona de guardado como atributo del ítem: nevera, congelador, despensa. El mismo
  producto tiene tres vidas útiles distintas.
- **Cambia** — El ajuste "de acuerdo a la temperatura" por un modelo de tres niveles: (a) tabla
  pública por producto y zona, que es lo posible hoy; (b) temperatura que declara el usuario una vez;
  (c) sensor Bluetooth real, en la versión 2. Solo el nivel (c) justifica decir "ajustado a tu
  nevera".
- **Cambia** — La alerta de "no se recomienda consumir" por una sugerencia de orden de consumo. La
  app sugiere qué aprovechar antes y dice qué cree con base en lo que el usuario registró, y nunca
  emite un juicio de inocuidad. Declarar algo apto para consumo es asumir responsabilidad civil si
  alguien enferma, y un descargo de "bajo riesgo del cliente" no borra ese deber si el diseño invitó
  a confiar. La salvedad correcta no es legal, es de honestidad de producto: la app lleva la cuenta,
  la persona ve, huele y decide.
- **Agrega** — Estado declarado por el usuario: `está bien` / `dudoso` / `ya no`. Recalcula el
  estimado, alimenta el registro de desperdicio y deja el juicio donde corresponde.
- **Agrega** — Distinción entre fecha de caducidad y fecha de consumo preferente. En la Unión
  Europea son dos categorías con significado distinto bajo el reglamento 1169/2011: *use by* es
  límite de seguridad, *best before* es calidad. Tratarlas igual hace tirar comida buena y avisar
  tarde de la peligrosa.

## FE2 · Recetas según inventario

Cambia de rol: deja de ser una feature de valor y pasa a ser el motor que mantiene vivo el
inventario.

- **Deja** — Las dos modalidades planteadas: cocinable con lo que hay, y cocinable comprando uno o
  dos secundarios. Formalizadas en tres cubetas: `cocinable ya`, `falta 1–2`, `falta lo principal`.
- **Deja** — Recetas de conocimiento general, con texto propio. Una boloñesa, un arroz con pollo o
  unos huevos revueltos no son de nadie: la lista de ingredientes y el procedimiento básico no son
  protegibles por derecho de autor. Ese repertorio cubre la mayoría de lo que se cocina en una casa.
- **Agrega** — "Cociné esto": un toque descuenta los ingredientes. Es la corrección más importante de
  todo el refinamiento, y no pide al usuario una tarea nueva porque ya estaba mirando la receta.
- **Agrega** — Los faltantes van directo a la lista de compras.
- **Agrega** — Enlace a blogs de cocina para las recetas específicas y de autor. Enlazar es legítimo;
  copiar no. Regla práctica: título, nombre del sitio, una línea de descripción y el enlace, sin
  reproducir el texto de preparación, sin traer las imágenes al servidor propio y sin mostrar la
  receta completa dentro de la app. Abre además alianzas con creadores, que quieren el tráfico.
- **Agrega** — Aviso visible de que la receta la genera un sistema de IA. El art. 50 de la Ley de IA
  de la Unión Europea obliga desde el 2 de agosto de 2026 a informar que se interactúa con IA y a
  marcar el contenido generado en formato legible por máquina; las multas llegan a 15 millones de
  euros o 3% de la facturación global.
- **Cambia** — "Sugerir recetas" por "qué aprovechar primero". El foco cambia y el tono también: la
  app habla de aprovechar, no de perder.
- **Cambia** — El emparejamiento por nombre por uno con cantidades. Saber que "hay pollo" no basta
  para proponer un plato que pide 500 g.
- **Quita** — Copiar el texto de preparación o las fotos de un blog al recetario propio. Lo protegido
  es la expresión, no la receta como idea.

### Vocabulario del producto

Las correcciones de tono de FE1 y FE2 son la misma decisión. Conviene fijarla antes de escribir la
primera pantalla, porque después es un rediseño.

| Situación | Así se dice | Así no |
|---|---|---|
| Sección de inicio | Aprovecha primero · En su mejor momento | Por vencer · A punto de echarse a perder |
| Ítem con pocos días | Mejor hoy o mañana | Se te va a perder |
| Sugerencia de plato | Con la espinaca de ayer sale bien esto | Salva tu espinaca antes de tirarla |
| Ítem pasado de fecha | Según lo que registraste, esto llevaba 2 días. Revísalo antes de usarlo | No consumir · Producto en mal estado |
| Estado del producto | Tú lo ves y lo hueles; nosotros llevamos la cuenta | Apto para consumo · Seguro |
| Estimación | Estimado según la fecha y el lugar donde lo guardaste | Vence el jueves, como hecho |
| Receta generada | Sugerencia generada con IA · Receta de *nombre del blog* | Nuestra receta, sobre contenido ajeno o generado |

## FE3 · Personalización nutricional

El encuadre acordado sirve: todo entra como preferencia declarada por el usuario, no como dato
clínico. Funciona bajo tres condiciones que no se pueden soltar.

- **Deja** — Alergias, intolerancias y gustos, con la distinción de comportamiento: alergia e
  intolerancia son filtro duro y excluyen la receta por completo; el disgusto es filtro suave y solo
  baja el orden.
- **Deja** — Perfil por miembro, no por hogar. El filtro duro de una comida es la unión de las
  alergias de todos los que van a comer, no la del que cocina.
- **Cambia** — El perfil clínico por un plan de alimentación que ingresa el propio usuario. La app no
  pregunta condiciones, no calcula nada médico y no ajusta el plan: recibe lo que la persona declara
  ("sin lácteos", "alto en proteína", "1 800 kcal", "cinco comidas") y filtra y ordena las
  sugerencias con eso.
- **Agrega** — Las tres condiciones que sostienen el encuadre, porque los reguladores miran la
  función y no el nombre del campo: (1) la app nunca pregunta por una enfermedad ni la registra;
  (2) nada de lenguaje clínico, umbrales, metas terapéuticas ni afirmaciones tipo "apto para
  diabéticos"; (3) la app nunca genera ni corrige un plan, solo ejecuta el que le dieron.
- **Agrega** — Alergias e intolerancias también como preferencia declarada, sin registrar el
  diagnóstico detrás. Matiz de manejo, no de producto: "sin gluten" puede revelar celiaquía, y en la
  Unión Europea un dato del que se infiere salud puede caer en categoría especial aunque el campo se
  llame preferencia. La respuesta es cifrado, sin publicidad segmentada, sin compartir con terceros y
  sin entrenar modelos con eso.
- **Agrega** — Comportamiento conservador ante datos incompletos: si no se conoce la composición de
  un producto, la app dice `no verificado — revisa la etiqueta` y nunca afirma que la receta es
  segura. Esa ruta necesita pruebas dedicadas y permanentes.
- **Agrega** — Perfiles de menores sin datos de salud. COPPA en Estados Unidos exige consentimiento
  verificable de los padres para menores de 13; el art. 8 del RGPD fija la edad de consentimiento
  entre 13 y 16 según el país; Colombia lo restringe en el art. 7 de la Ley 1581.
- **Agrega** — Versión 3: el nutricionista como cliente. El profesional carga el plan y el paciente lo
  recibe en su app. La prescripción sigue siendo del profesional.
- **Quita de la versión 1** — Los campos clínicos: peso, índice de masa corporal y condiciones
  médicas registradas como tales. Cuatro motivos legales concretos:
  - **Unión Europea.** Son datos de salud, categoría especial del art. 9 del RGPD: consentimiento
    explícito, evaluación de impacto y minimización. Y bajo la regla 11 del anexo VIII del MDR, el
    software de asesoría nutricional presentado para gestionar una enfermedad como la diabetes se
    clasifica como clase IIa, lo que implica marcado CE, sistema de gestión de calidad y evaluación
    clínica: meses y decenas de miles de euros antes de vender una suscripción. La misma función
    descrita como bienestar general queda fuera.
  - **Estados Unidos.** La ley My Health My Data del estado de Washington cubre datos de salud del
    consumidor, incluye inferencias sobre condiciones y trae derecho privado de acción, es decir
    demandas colectivas sin necesidad de un regulador. La regla de notificación de brechas de la FTC
    aplica a apps de salud que no están bajo HIPAA.
  - **México.** La LFPDPPP de marzo de 2025 trajo penas penales, tribunales federales especializados
    y multas duplicadas para infracciones sobre datos sensibles.
  - **Colombia.** La Ley 1581 de 2012 prohíbe tratar datos sensibles salvo autorización explícita,
    obliga a registrar las bases ante la SIC, y su art. 7 restringe el tratamiento de datos de
    menores.

## FE4 · Sugerencias de compra

Es la feature que la gente realmente quiere. Solo hay que sacarle un supuesto equivocado.

- **Deja** — Lista generada cuando algo se agota o está por vencer, apoyada en hábitos de consumo del
  hogar, y la exclusión explícita del usuario.
- **Cambia** — Por lo que el usuario marca como importante, y de ahí en adelante por lo que hace. Una
  estrella en "esto nunca puede faltar" resuelve la primera semana sin adivinar nada. Tras tres o
  cuatro compras, la frecuencia de recompra de esa casa predice mejor que cualquier catálogo.
- **Cambia** — "Sugerir compras" por una sola lista viva, siempre disponible, en vez de una
  notificación que sugiere y se pierde.
- **Agrega** — Lista compartible al grupo de WhatsApp de la casa.
- **Agrega** — Declaración de comisión si la sugerencia está patrocinada o genera afiliación. Las
  guías de la FTC sobre endosos en Estados Unidos y las normas de prácticas comerciales desleales en
  la Unión Europea exigen que la relación comercial sea evidente.
- **Quita** — La lista de alimentos "principales", en cualquier versión. Ni global ni por país: los
  básicos de una casa mexicana, colombiana y estadounidense no coinciden (tortilla, arepa, pan), y
  dentro del mismo país tampoco coinciden dos casas.

### Qué significa "lista viva"

Es la diferencia entre una notificación y una pantalla. La notificación aparece una vez, se pierde
si no se ve en el momento y no acumula nada. La lista viva es un solo lugar que siempre está ahí,
siempre actualizado, y al que el usuario entra por su propia voluntad camino al supermercado.

| Aspecto | Cómo se comporta |
|---|---|
| De dónde salen los ítems | Se agotó en el inventario · está por vencer y es algo que se repone siempre · falta para una receta elegida · lo agregó alguien de la casa a mano o por voz |
| Estados de cada ítem | `sugerido` (la app lo propuso) · `confirmado` (alguien lo aprobó) · `comprado` (se marca en la tienda y entra al inventario) |
| Quién la ve | Todo el hogar, en tiempo real |
| Cómo se ordena | Por categoría o pasillo, no por fecha de agregado |
| En la tienda | Funciona sin conexión y en una sola pantalla |
| Al terminar | Lo marcado se convierte en inventario; lo no comprado permanece para la próxima. Nunca se vacía ni se reinicia |

## FE5 · Integración con apps de domicilio

Ver [03-integraciones-compra.md](03-integraciones-compra.md) para el detalle completo: los diez
aspectos de la limitante, la escalera de opciones, el catálogo de plataformas y los bloqueos.

Resumen: fuera de la versión 1, pero viva como objetivo. Se conserva el objetivo de que el usuario
pase de la lista a la compra sin retipear nada, y se cumple hoy con enlace profundo, portapapeles,
WhatsApp y programa de afiliados. Se quita la expectativa de que Rappi o Uber Eats tengan una API de
consumidor: no la tienen, aunque Instacart y Kroger sí, lo que demuestra que el objetivo no es
fantasía.

## FE6 · Perfiles familiares (nueva)

Ver [04-perfiles-familiares.md](04-perfiles-familiares.md).

## Correcciones que entran a la versión 1

| Corrección | Sobre | Por qué entra |
|---|---|---|
| "Cociné esto" descuenta inventario | FE2 | Es el mecanismo de descarga que faltaba |
| Fecha de apertura del envase | FE1 | Es la diferencia entre "5 días" y "3 semanas" en el mismo producto |
| Zona de guardado por ítem | FE1 | Tres vidas útiles distintas para el mismo alimento |
| Sugerencia de orden de consumo, sin veredicto, con estado declarado por el usuario | FE1 | Responsabilidad civil en EEUU y riesgo de propósito médico en la UE |
| Caducidad frente a consumo preferente | FE1 | Categorías legalmente distintas en la UE (reglamento 1169/2011) |
| Ticket primero, voz como excepción | Captura | Treinta ítems por foto contra tres por nota de voz |
| La voz se queda; se borra el audio, no la función | Captura | Grabar no es tratar un dato biométrico; el riesgo está en retención, revisión humana, entrenamiento y menores |
| Clásicos con texto propio, blogs por enlace | FE2 | La receta como idea no es protegible; la redacción y las fotos sí |
| Vocabulario de "aprovecha primero" | FE1 · FE2 | El tono negativo desmotiva; el positivo dice lo mismo y se sostiene mejor |
| Plan y restricciones como preferencia declarada, sin campos clínicos | FE3 | RGPD art. 9 y MDR regla 11; My Health My Data; LFPDPPP; Ley 1581 |
| Aviso de contenido generado por IA | FE2 | Art. 50 de la Ley de IA de la UE, vigente desde el 2 de agosto de 2026 |
| Sin lista de básicos: el usuario marca qué le importa | FE4 | "Global" no existe en alimentación, y ni siquiera "por país" |
| Enlace profundo en vez de API de delivery | FE5 | Los diez aspectos del documento de integraciones |

## Features nuevas para la versión 1

1. **Registro de desperdicio con dinero.** "Tiré esto" en dos toques y un contador mensual. Prueba de
   valor, gancho de retención y, más adelante, el número con el que se vende y se levanta capital.
   Si solo se agrega una feature nueva, es esta.
2. **Sobras como ítem de primera clase**, con caducidad por defecto de tres días. Es donde más se
   desperdicia y donde ninguna app basada en códigos de barras ayuda.
3. **Pantalla "usa esto hoy"** como inicio, en lugar de la lista de inventario.
4. **Hogar compartido con roles**: a quien va al súper le llega la lista; a quien cocina, qué usar.
5. **Perfiles familiares (FE6)** con tres listas de ingredientes por persona y selector de comensales.
6. **Lista por WhatsApp**, y evaluar que la captura por nota de voz a un número sea la versión 1
   completa, sin app que instalar.
7. **Modo congelador** con fecha de congelación y "úsalo antes de".
8. **Funcionamiento sin conexión y en Android de gama baja.**

Fuera de la versión 1, a propósito: sensores y hardware; integración por API con plataformas de
domicilio; campos clínicos y canal de nutricionistas; restaurantes y hoteles; cámara dentro de la
nevera.

## Hoja de ruta

| Cuándo | Qué | Por qué es factible y qué aporta |
|---|---|---|
| v2, ~6 meses | Sensor Bluetooth de temperatura con alerta de excursión térmica | Sensor comercial de USD 10–25 certificado como compatible, sin fabricar nada. Habilita la promesa original de FE1 y el aviso de corte de frío |
| v2 | Importación desde programas de fidelidad de retail | La jugada de Kitche trasladada a Puntos Colombia, Soriana o Walmart. Carga inicial sin trabajo |
| v2 | Plan semanal de comidas y presupuesto | La lista de compras pasa a ser la diferencia entre el plan y el inventario |
| v2 | Base de productos colaborativa | Lo que un usuario corrige mejora a todos. Sembrada desde Open Food Facts. Es el foso real |
| v2 | Etiquetas NFC o QR para recipientes | Menos de un dólar por etiqueta; un toque registra las sobras |
| v3, B2B | Restaurante mediano: etiquetas FEFO, bitácora de temperatura y costo de merma | Donde está el dinero. Los sistemas con cámara reportan retorno en 1,1 a 1,8 meses y se venden por cotización; el restaurante de 3 a 20 sedes queda fuera por precio |
| v3 | Canal de nutricionistas, con el profesional como cliente | Recupera la parte valiosa de FE3 sin emitir la indicación |
| v3 | Licenciamiento a fabricantes de electrodomésticos | Los que no son Samsung necesitan software que diferencie sus neveras |
| Futuro, sin fecha | Habilitar el carrito dentro de la plataforma (Rappi, Uber Eats y otras) y donación de excedentes | Se lista con dependencia, no con fecha: la primera depende del programa de socios de cada plataforma, que se habilita por volumen; la segunda, de densidad de vecinos |

Antes de construir cualquiera de estas: la prueba de conserje. Diez familias, dos semanas, notas de
voz a un número de WhatsApp y alguien del equipo registrando a mano. Responde la única pregunta que
decide si el producto existe (¿la gente registra lo que consume?) sin escribir una línea de
producto. La métrica que importa no es usuarios activos, es exactitud del inventario al día 30.
