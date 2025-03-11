# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Navigation.py'],
    pathex=[],
    binaries=[],
    datas=[('BD/basedatos.py', 'BD'), ('models/cliente.py', 'models'), ('recursos/iconos/engranaje.png', 'recursos/iconos'), ('recursos/iconos/usuario.png', 'recursos/iconos'), ('recursos/media/billete.jpg', 'recursos/media'), ('recursos/media/fondo.jpg', 'recursos/media'), ('billete_ui.py', '.'), ('billete.ui', '.'), ('compra.py', '.'), ('compras_ui.py', '.'), ('compras.ui', '.'), ('configuracion_ui.py', '.'), ('configuracion.py', '.'), ('configuracion.ui', '.'), ('firebase.txt', '.'), ('recursos/iconos/icon.ico', 'recursos/iconos'), ('login_ui.py', '.'), ('login.py', '.'), ('login.ui', '.'), ('menu_ui.py', '.'), ('menu.ui', '.'), ('menu.py', '.'), ('misviajes_ui.py', '.'), ('misviajes.ui', '.'), ('misviajes.ui', '.'), ('recursos_rc.py', '.'), ('recursos.qrc', '.'), ('viajes.db', '.'), ('vuelos_ui.py', '.'), ('vuelos.py', '.'), ('vuelos.ui', '.'), ('managerPDF/recursos/BilleteInfo.md', 'managerPDF/recursos'), ('managerPDF/recursos/destinosVigentes.md', 'managerPDF/recursos'), ('managerPDF/recursos/informacionUsuario.md', 'managerPDF/recursos'), ('managerPDF/recursos/MisViajesInfo.md', 'managerPDF/recursos'), ('managerPDF/recursos/VuelosInfo.md', 'managerPDF/recursos'), ('managerPDF/logo_alberti.png', 'managerPDF'), ('managerPDF/logo.png', 'managerPDF'), ('managerPDF/ManagerPDF.py', 'managerPDF'), ('recursos/informe1.png', 'recursos')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Skyberia',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['recursos\\iconos\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Skyberia',
)
