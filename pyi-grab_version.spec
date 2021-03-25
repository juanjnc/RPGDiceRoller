# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['pyi-grab_version', 'RPGDiceRoller2.spec'],
             pathex=['C:\\Users\\shurk\\PycharmProjects\\RPGDiceRoller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=True,
             win_private_assemblies=True,
             cipher=block_cipher,
             noarchive=False)
a.datas += [("./ico.ico", "ico.ico", "DATA")]
a.datas += [("./CHANGELOG.txt", "CHANGELOG.txt", "DATA")]
a.datas += [("./VC_redist.x64.exe", "VC_redist.x64.exe", "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='pyi-grab_version',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pyi-grab_version')
