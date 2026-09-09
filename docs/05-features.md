# Features de Freezai — alcance funcional consolidado

11 áreas funcionales, 73 features, 51 de ellas en la versión 1.

Fases: **v1** primera entrega · **v2** segunda entrega, con hardware opcional y datos de retail ·
**Futuro** habilitado por socios y canales nuevos.

## 1. Captura de datos

Tres vías para que la comida entre al inventario sin llenar formularios, más el retorno automático de
lo que se compró en línea.

| Feature | Qué hace | Fase |
|---|---|---|
| Dictado por voz | El usuario dice lo que guardó y la app extrae producto, cantidad y fecha | v1 |
| Foto del ticket | Una foto carga toda la compra; los ítems entran como borrador editable | v1 |
| Escaneo de código de barras | Agrega un producto puntual con su ficha completa | v1 |
| Entrada manual | Disponible siempre, como alternativa | v1 |
| Comprobante de compra en línea | El usuario comparte el correo del pedido y los productos entran al inventario, ya con los cambios del repartidor | v1 |
| Diccionario que aprende | Cada corrección mejora el reconocimiento de los nombres abreviados de su supermercado | v1 |
| Importación desde fidelidad | El usuario conecta su cuenta del súper y la compra aparece sola | v2 |

## 2. Inventario

El estado de la cocina, compartido por toda la casa y siempre al día.

| Feature | Qué hace | Fase |
|---|---|---|
| Ficha por producto | Cantidad, zona, fecha impresa, fecha de apertura y estado declarado | v1 |
| Tres zonas de guardado | Nevera, congelador y despensa, con vida útil propia por zona | v1 |
| Vida útil estimada | Para frescos sin fecha impresa, por producto y zona | v1 |
| Recalculo al abrir | "Abierto hoy" ajusta la estimación | v1 |
| Sobras como producto propio | Registro por voz o etiqueta, con caducidad automática de tres días | v1 |
| Modo congelador | Fecha de congelación y aviso de "úsalo antes de" | v1 |
| Inventario compartido | Todos los miembros ven y editan el mismo estado en tiempo real | v1 |
| Estado declarado | `está bien`, `dudoso` o `ya no` ajustan la estimación con un toque | v1 |
| Funciona sin conexión | Consulta y edición con señal intermitente | v1 |

## 3. Caducidad y prioridad de consumo

| Feature | Qué hace | Fase |
|---|---|---|
| Aprovecha primero | Orden FEFO: lo que vence primero se propone primero | v1 |
| Inicio con lo del día | Tres productos para aprovechar y tres cosas que hacer con ellos | v1 |
| Avisos oportunos | Notificación cuando algo entra en sus últimos días | v1 |
| Temperatura declarada | El usuario indica la temperatura de su nevera y las estimaciones se ajustan | v1 |
| Sensor Bluetooth de temperatura | Vida útil ajustada a la temperatura real medida | v2 |
| Alerta de corte de frío | Aviso tras un corte de luz o una puerta mal cerrada | v2 |

## 4. Recetas y qué cocinar

| Feature | Qué hace | Fase |
|---|---|---|
| Tres niveles de disponibilidad | `cocinable ya`, `falta 1–2`, `falta lo principal` | v1 |
| Orden por conveniencia | Primero los platos que usan lo que está en su mejor momento | v1 |
| Cociné esto | Un toque descuenta los ingredientes del inventario | v1 |
| Faltantes a la lista | Lo que falte para la receta elegida pasa a la lista de compras | v1 |
| Recetario propio de clásicos | Platos de todos los días, con texto propio y cantidades de la casa | v1 |
| Recetas de creadores | Enlace a blogs y sitios de cocina, con crédito visible | v1 |
| Ajuste de porciones | La receta se escala según cuántos comen | v1 |
| Plan semanal de comidas | Menú de la semana desde el inventario | v2 |

## 5. Perfiles familiares

| Feature | Qué hace | Fase |
|---|---|---|
| Tres listas por persona | `no puede` excluye, `evita` baja, `le encanta` sube. Más notas libres | v1 |
| Presets de un toque | Vegetariano, vegano, sin cerdo, halal, kosher, sin lácteos, sin gluten, sin frutos secos, sin mariscos, sin picante | v1 |
| Jerarquía de ingredientes | Cada restricción cubre derivados: "sin lácteos" arrastra mantequilla, crema, queso y suero | v1 |
| Selector de comensales | El filtro de la comida es la unión de las restricciones de los presentes | v1 |
| Escenas guardadas | Cena familiar, solo adultos, los niños, solo yo, invitado temporal | v1 |
| Matriz de quién come qué | Miembros y categorías de ingredientes en una sola vista | v1 |
| Motivo visible por receta | `sirve para Ana y Luis · no para Sofía (maní)` | v1 |
| Sustituciones sugeridas | Leche por bebida vegetal, crema por coco, antes de descartar | v1 |
| Aprende de lo que se cocina | Un pulgar por miembro ajusta gustos y disgustos | v1 |

## 6. Plan de alimentación

| Feature | Qué hace | Fase |
|---|---|---|
| Plan declarado por el usuario | "Sin lácteos", "alto en proteína", "1 800 kcal": la app filtra y ordena con él | v1 |
| Preferencias por miembro | Cada persona con su propio plan y sus metas | v1 |
| Información nutricional | Macros y porciones por plato | v2 |
| Canal de nutricionistas | El profesional carga el plan y la app lo ejecuta en la cocina | Futuro |

## 7. Lista de compras

| Feature | Qué hace | Fase |
|---|---|---|
| Lista viva | Se alimenta de lo agotado, lo por vencer que se repone, los faltantes de receta y lo que agrega la casa | v1 |
| Estados por ítem | `sugerido`, `confirmado`, `comprado`; lo comprado entra al inventario | v1 |
| Imprescindibles marcados | Una estrella en lo que nunca puede faltar; luego la app aprende de la recompra | v1 |
| Orden por pasillo | Agrupada por categoría para recorrer el súper una sola vez | v1 |
| Compartida en tiempo real | Quien va al súper marca y el resto lo ve al instante | v1 |
| Envío por WhatsApp | Al grupo de la casa o al chat del tendero | v1 |
| Presupuesto semanal | Cuánto va costando la lista y cómo se compara | v2 |
| Comparación de precios | Dónde conviene comprar la canasta de la semana | v2 |

## 8. Compra del faltante

| Feature | Qué hace | Fase |
|---|---|---|
| Salida a la plataforma de domicilio | Rappi, PedidosYa, Uber Eats, DiDi Food o la app del súper se abren con los productos ya identificados | v1 |
| Pedido al tendero por WhatsApp | La lista se envía como mensaje al comercio del barrio | v1 |
| Lista al portapapeles | Copiar toda la compra en un toque | v1 |
| Retorno por comprobante | El correo o la pantalla del pedido entran al inventario con fecha estimada | v1 |
| Programa de afiliados | Los enlaces generan comisión por pedido, con la relación declarada al usuario | v1 |
| Carrito armado dentro de la plataforma | Habilitar el carrito completo en Rappi, Uber Eats y otras plataformas de domicilio, sujeto al programa de socios de cada una, que se abre por volumen de pedidos generados. El diseño lo contempla desde ahora | Futuro |
| Integración con retailer directo | Catálogo, precios y carrito con Éxito, Cencosud, Soriana o Chedraui | Futuro |
| Middleware de receta a carrito | Un acuerdo con un intermediario habilita decenas de retailers | Futuro |

## 9. Ahorro y desperdicio

| Feature | Qué hace | Fase |
|---|---|---|
| Tiré esto | Registrar lo botado en dos toques, con el motivo | v1 |
| Contador de dinero | Cuánto se desperdició y cuánto se aprovechó este mes | v1 |
| Reporte mensual del hogar | Qué se pierde con más frecuencia y en qué categoría | v1 |
| Meta de reducción | El hogar fija una meta y ve el avance semanal | v2 |
| Donación de excedentes | Ofrecer a vecinos lo que no se va a consumir a tiempo | Futuro |

## 10. Hardware opcional

Accesorios comerciales que la app reconoce. Ninguno es necesario para usar el producto.

| Feature | Qué hace | Fase |
|---|---|---|
| Sensor Bluetooth de temperatura y humedad | Modelos comerciales de 10 a 25 dólares certificados como compatibles | v2 |
| Etiquetas NFC o QR para recipientes | Un toque registra las sobras | v2 |
| Báscula Bluetooth de cocina | Cantidades exactas al guardar y al servir | v2 |
| Impresora térmica de etiquetas | Etiqueta con producto, fecha, hora y responsable | Futuro |

## 11. Canal profesional

| Feature | Qué hace | Fase |
|---|---|---|
| Etiquetado FEFO de preparaciones | Cada preparación sale etiquetada con fecha, hora y responsable | Futuro |
| Bitácora de temperatura | Registro continuo y exportable, listo para inspección | Futuro |
| Costo de merma | Cuánto se pierde, en qué insumo y en qué turno | Futuro |
| Multi-sede | Varias cocinas bajo una sola vista de operaciones | Futuro |
| Licenciamiento a fabricantes | El inventario inteligente dentro de la app de un fabricante | Futuro |

## Base común a todas las features

Español y localización por país, con nombres de producto y unidades del mercado donde se usa.
Funciona en teléfonos de gama baja y sin conexión. Base de productos que mejora con cada corrección
de los usuarios. Todo el contenido generado se identifica como tal, y las estimaciones se presentan
como estimaciones: la app lleva la cuenta y la persona decide.
