BULLY-centric branch to fix issues.
I am not paying attention to other game support. Stuff may have gotten broken.

# Fixes:
- Model texture flags are no longer reset to 0 from 12800 after export
- NiStringExtraData are preserved on export
- Material names should no longer screw with texture assignments upon import
- Cube maps should no longer be lost
- NiSpecular Property should no longer be defaulted to 1 for every mesh after export (done by stripping it to meshes lacking a _s texture. Beware of rare naming inconsistencies though)

Known Issues:
- NiStencilPropery may be reset to 0 on export?