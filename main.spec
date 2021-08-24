# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
spec_root = os.path.abspath(SPECPATH)


a = Analysis(['main.py'],
             pathex=[spec_root],
             binaries=[],
             datas=[],
             hiddenimports=[
                'uvicorn.logging', 'dependency_injector.errors', 'dependency_injector.errors',
                'dependency_injector.providers', 'dependency_injector.containers', 'six', 'json'
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
