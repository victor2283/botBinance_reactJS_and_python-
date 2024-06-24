# botBinance_reactJS_and_python-
una version para escritorio del bot de binance que usa react js como interfaz grafica y django
modo de uso:
la app principal en este caso sera nav.py que es una app basica que usa el frontend desarrollado con react js ya compilado y puesto en django por eso la app busca la direccion http://localhost:8000 al inicial , los graficos fueron desarrollados con plotly js a diferencia de la otra app que tambien dejo dispoble de entorno grafico de python que se llama app.py en el directorio raiz. bueno esta app nav.py tiene una app que sincroniza la hora actual en caso de error del servidor de binance sync_time.py cuya clase es importada en el bot.py que es la app que hace la magia de toda la app en todas sus versiones haciendo las ordenes de compra y de venta en forma automatica y es donde debe corregir el codigo para su propia estrategia de trading en caso que lo requiera o ajustar el par. Esta version nav.py es mucho mejor que la otra app.py porque nunca se desconecta en caso de error solo avisa errores del servidor y reintenta gracias a django en modo servidor, y por medio de react js la pagina siempre esta mostrando informacion actualizada sin afectar los procesos y puede cancelar al bot desde un boton que puse en la aplicacion que desactiva la aplicacion de react js.
El modo de ejecutar la aplicacion es simplemente poneindo en consola : py nav.py 
como le recomiendo ir a la carpeta front end antes de empezar y compilar nuevamente usando npm run build aunque deje en la carpeta static de django los archivos necesarios para que la app funcione esto esta en la carpeta backend /static/ y en template/ esta el archivo html que usa django para la aplicacion nav al llamar a localhost:8000 

cualquier colaboracion por la causa o donacion recibo en victor2283@gmailcom en cualquiera de mis cuentas de pago (skrill, binance pay, airtm) o puede enviarme un email para solicitarme mi cvu o cbu si quiere colaborar con dinero via transferencia bancaria internacional.
