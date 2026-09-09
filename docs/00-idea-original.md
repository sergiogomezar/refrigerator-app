# Idea refinement

## 1. Idea principal
Crear una aplicación para gestión de compras en refrigerador.

## 2. Descripción
- Usuarios: app móvil para familias. Expandible a restaurantes, hoteles.
- Problema: evitar que la comida caduque.
- Alcance: inventario de la nevera (qué hay, cuándo se vence), sugerencias de compra, gestión de alimentación.
- Captura de datos: evitar formularios. Preferencia por audio u otro método de baja friccion (pendiente de decidir).
- Plataforma: móvil principal. Web por explorar.

## 3. Features

### Captura de datos (decidido)
- Captura por voz: transcripcion + extraccion de item, cantidad, caducidad.
- Foto del ticket de compra: OCR para carga masiva.
- Entrada manual: solo como fallback de ultimo recurso. No promoverla en la interfaz.

### Features base (propuestas, no confirmadas por el usuario)
- Inventario de nevera con fecha de caducidad por item.
- Alertas push de vencimiento proximo.
- Lista de compras auto-sugerida por consumo y faltantes.
- Perfiles de familia: inventario compartido entre varios miembros.
- Sugerencia de recetas con lo que esta por vencer.

### Features especificas del usuario

#### FE1. Gestion de caducidad y priorizacion de consumo
- Saber cuando un alimento esta proximo a vencerse.
- Alimentos frescos sin fecha impresa (vegetales, frutas, huevos): estimar vida util segun temperatura de la nevera.
- Sugerir que alimentos consumir o usar primero (orden FEFO: first expired, first out).
- Alertas de alimentos expirados o no recomendados para consumo, bajo riesgo del usuario.

Notas de diseno abiertas:
- Fuente de la temperatura: valor fijo por zona de la nevera, entrada manual del usuario, o sensor IoT/termometro bluetooth.
- Base de datos de vida util por producto y zona (nevera, congelador, despensa) mas ajuste por temperatura.
- Registro de fecha de apertura: la vida util cambia al abrir el envase.
- Aviso legal necesario: la app da estimados, no garantiza inocuidad alimentaria. Exclusion de responsabilidad y lenguaje no medico.

#### FE2. Sugerencia de recetas segun inventario
- Sugerir recetas o platos con base en los ingredientes que ya estan en el inventario.
- Cubrir tambien recetas donde los ingredientes principales estan en la nevera y algunos secundarios u opcionales hay que comprar.
- Fuerte acoplamiento con FE1: priorizar recetas que consuman lo que esta proximo a vencer.

Notas de diseno abiertas:
- Modelo de match: por receta, calcular cobertura de ingredientes. Distinguir ingrediente principal, secundario y opcional.
- Clasificar resultados: "cocinable ya", "falta 1-2 items", "falta lo principal".
- Los faltantes alimentan la lista de compras (enlace con la feature de lista sugerida).
- Fuente de recetas: base propia curada, API externa (Spoonacular, Edamam), o generacion por LLM. Decision pendiente.
- Normalizacion de ingredientes: "pechuga de pollo" vs "pollo" vs "muslo". Requiere taxonomia o embeddings para el match.
- Cantidades: saber si hay suficiente, no solo si el ingrediente existe.

#### FE3. Personalizacion nutricional de las recetas
Modifica el ranking de FE2 segun el perfil de cada miembro de la familia:
- Indicaciones de un nutricionista (plan externo cargado en la app).
- Peso e indice de masa corporal.
- Condiciones medicas: diabetes, intolerancia a la lactosa, alergias.
- Gustos y disgustos.

Distincion critica de comportamiento:
- Alergias e intolerancias son filtros duros: excluyen la receta por completo, nunca la degradan en el ranking.
- Disgustos y preferencias son filtros suaves: bajan el puesto pero siguen visibles.
- Diabetes y metas de peso ajustan el orden y muestran informacion nutricional, no bloquean.

Notas de diseno abiertas:
- Perfil por miembro, no por hogar. Una cena tiene que satisfacer varios perfiles a la vez: el filtro duro es la union de todas las alergias de quienes comen.
- Alergenos ocultos: requiere datos de ingredientes a nivel de producto, no solo el nombre del plato. Es el punto mas dificil de esta feature.
- Datos nutricionales por receta: necesita fuente con macros por ingrediente y porcion.
- Ingesta del plan del nutricionista: PDF, entrada manual, o plantillas de dietas comunes.

Riesgo y cumplimiento:
- Peso, IMC y condiciones medicas son datos de salud. Bajo GDPR son categoria especial y exigen consentimiento explicito, cifrado y minimizacion. Revisar tambien normativa local (Colombia, Mexico, EEUU segun mercado).
- La app no debe presentar consejo medico ni nutricional profesional. Posicionarla como asistente que aplica un plan que ya dio un profesional.
- Un fallo en el filtro de alergias puede causar dano fisico. Necesita tests dedicados, aviso de "verifica siempre la etiqueta" y comportamiento conservador ante datos incompletos: si el alergeno es desconocido, no afirmar que la receta es segura.

#### FE4. Sugerencias de compra
Basada en FE1 (inventario y caducidad).
- Existe un conjunto de alimentos considerados basicos o staples que normalmente deberian comprarse, salvo indicacion explicita del usuario de excluirlos.
- Cuando un alimento esta proximo a vencer o se agota el inventario, generar una lista de compras sugerida.
- La sugerencia se apoya en habitos de consumo del hogar (frecuencia y cantidad con que se repone y se consume cada item).

#### FE5. Integracion con apps de domicilio
- Integrar con plataformas de entrega y compra de mercado: Rappi, Uber Eats, DiDi Food, y similares.
- Objetivo: que el usuario pueda comprar los alimentos de la lista sugerida (FE4) directamente desde la app.

### Estado
Lista de features CERRADA por el usuario. 5 features especificas (FE1-FE5) mas la decision de captura de datos.

## 4. Siguiente paso solicitado
(pendiente)
