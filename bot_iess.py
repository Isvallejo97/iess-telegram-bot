# Bot de Telegram para Servicios del IESS
# Instalación: pip install python-telegram-bot

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = '8058585636:AAHBgSWAPjhXAamiPHJdjVm5Nnx61k9B5KM'

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📋 Servicios en Línea", callback_data='servicios')],
        [InlineKeyboardButton("👤 Afiliación", callback_data='afiliacion')],
        [InlineKeyboardButton("🏥 Citas Médicas", callback_data='citas')],
        [InlineKeyboardButton("💰 Pensiones", callback_data='pensiones')],
        [InlineKeyboardButton("📞 Contacto IESS", callback_data='contacto')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    mensaje = """
🏛️ **Bienvenido al Bot del IESS**

Soy tu asistente virtual para consultas sobre los servicios del Instituto Ecuatoriano de Seguridad Social.

¿En qué puedo ayudarte hoy?
    """
    await update.message.reply_text(mensaje, reply_markup=reply_markup, parse_mode='Markdown')

# Manejador de botones
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'servicios':
        mensaje = """
📋 **Servicios en Línea del IESS**

• Trámites Virtuales
• Consulta de Aportes
• Certificados en Línea
• Estado de Trámites
• Turnos en Línea

🔗 Portal: https://www.iess.gob.ec/tramites-virtuales/
        """
        keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='volver')]]
        
    elif query.data == 'afiliacion':
        mensaje = """
👤 **Afiliación al IESS**

**¿Cómo afiliarse?**
1. Ingresa a: https://app.iess.gob.ec/
2. Selecciona "¡Afíliate ya!"
3. Completa el formulario
4. Presenta documentos requeridos

**Tipos de afiliación:**
• Seguro General
• Seguro Voluntario
• Seguro Campesino
• Afiliación Joven

📞 Más info: 1800-IESS-900
        """
        keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='volver')]]
        
    elif query.data == 'citas':
        mensaje = """
🏥 **Citas Médicas IESS**

**Agendar cita:**
📱 Llama al 140
🌐 En línea: https://app.iess.gob.ec/iess-gestion-agendamiento-citas-medicas-web/

**Horarios:**
• Lun-Vie: 7:00 - 19:00
• Sáb-Dom: 8:00 - 14:00

**Requisitos:**
✓ Cédula de identidad
✓ Número de afiliado
✓ Estar al día en aportes
        """
        keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='volver')]]
        
    elif query.data == 'pensiones':
        mensaje = """
💰 **Pensiones IESS**

**Tipos de pensiones:**
• Jubilación por vejez
• Jubilación por invalidez
• Montepío (viudez/orfandad)

**Requisitos básicos jubilación:**
• 60 años cumplidos
• Mínimo 360 imposiciones
• O 40 años de edad + 480 imposiciones

📋 Consulta tu historial:
https://www.iess.gob.ec/aplicaciones/AfiliacionIESS/

☎️ Información: 1800-IESS-900
        """
        keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='volver')]]
        
    elif query.data == 'contacto':
        mensaje = """
📞 **Contacto IESS**

**Línea de atención:**
📱 140 (Citas médicas)
📞 1800-IESS-900

**Oficinas de atención:**
Lunes a Viernes: 8:00 - 17:00

**Redes sociales:**
🌐 www.iess.gob.ec
📧 Consultas en línea disponibles

**Turnos en línea:**
https://app.iess.gob.ec/iess-gestion-turnero-enlinea-web/
        """
        keyboard = [[InlineKeyboardButton("⬅️ Volver", callback_data='volver')]]
        
    elif query.data == 'volver':
        keyboard = [
            [InlineKeyboardButton("📋 Servicios en Línea", callback_data='servicios')],
            [InlineKeyboardButton("👤 Afiliación", callback_data='afiliacion')],
            [InlineKeyboardButton("🏥 Citas Médicas", callback_data='citas')],
            [InlineKeyboardButton("💰 Pensiones", callback_data='pensiones')],
            [InlineKeyboardButton("📞 Contacto IESS", callback_data='contacto')]
        ]
        mensaje = "¿En qué más puedo ayudarte?"
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(mensaje, reply_markup=reply_markup, parse_mode='Markdown')

# Comando /ayuda
async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = """
📖 **Comandos disponibles:**

/start - Menú principal
/ayuda - Ver esta ayuda
/servicios - Servicios en línea
/afiliacion - Info sobre afiliación
/citas - Agendar citas médicas
/pensiones - Info sobre pensiones
/contacto - Contactos del IESS

💡 También puedes escribir tu consulta directamente.
    """
    await update.message.reply_text(mensaje, parse_mode='Markdown')

# Comandos directos
async def servicios_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔗 Ver portal", url='https://www.iess.gob.ec/tramites-virtuales/')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mensaje = "📋 Accede a todos los servicios en línea del IESS:"
    await update.message.reply_text(mensaje, reply_markup=reply_markup)

async def afiliacion_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔗 Afiliarse ahora", url='https://app.iess.gob.ec/')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mensaje = "👤 Inicia tu proceso de afiliación aquí:"
    await update.message.reply_text(mensaje, reply_markup=reply_markup)

async def citas_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📱 Agendar cita", url='https://app.iess.gob.ec/iess-gestion-agendamiento-citas-medicas-web/')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mensaje = "🏥 Agenda tu cita médica o llama al 140:"
    await update.message.reply_text(mensaje, reply_markup=reply_markup)

# Mensaje por defecto
async def mensaje_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    
    if 'cita' in texto or 'médica' in texto or 'doctor' in texto:
        await citas_cmd(update, context)
    elif 'afiliar' in texto or 'afiliación' in texto or 'inscribir' in texto:
        await afiliacion_cmd(update, context)
    elif 'pensión' in texto or 'jubilación' in texto or 'retirar' in texto:
        keyboard = [[InlineKeyboardButton("💰 Ver info", callback_data='pensiones')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Información sobre pensiones:", reply_markup=reply_markup)
    elif 'contacto' in texto or 'teléfono' in texto or 'llamar' in texto:
        await update.message.reply_text("📞 Líneas de atención:\n• 140 (Citas)\n• 1800-IESS-900 (Información)")
    else:
        await update.message.reply_text("No entendí tu consulta. Usa /ayuda para ver los comandos disponibles o /start para el menú principal.")

def main():
    print("🤖 Iniciando bot del IESS...")
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(CommandHandler("servicios", servicios_cmd))
    app.add_handler(CommandHandler("afiliacion", afiliacion_cmd))
    app.add_handler(CommandHandler("citas", citas_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje_texto))
    
    print("✅ Bot activo y escuchando...")
    app.run_polling()

if __name__ == '__main__':
    main()
