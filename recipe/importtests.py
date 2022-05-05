import os
import vtk
import traceback
print("Common")
from vmtk.vtkvmtkCommonPython import *
print("Computational Geometry")
from vmtk.vtkvmtkComputationalGeometryPython import *
print("Differential Geometry")
from vmtk.vtkvmtkDifferentialGeometryPython import *
print("IO")
from vmtk.vtkvmtkIOPython import *
print("Misc")
from vmtk.vtkvmtkMiscPython import *
print("Rendering")
try:
    from vmtk.vtkvmtkRenderingPython import *
except:
    print("No rendering backend")
    print(traceback.format_exc())  
    pass
print("Segmentation")
from vmtk.vtkvmtkSegmentationPython import *
print("ITK")
from vmtk.vtkvmtkITKPython import *
try:
    from vmtk.vtkvmtkContribPython import *
except:
    pass


__all__ = [
    'vmtk.vmtkactivetubes',
    'vmtk.vmtkbifurcationprofiles',
    'vmtk.vmtkbifurcationreferencesystems',
    'vmtk.vmtkbifurcationsections',
    'vmtk.vmtkbifurcationvectors',
    'vmtk.vmtkboundarylayer',
    'vmtk.vmtkboundaryreferencesystems',
    'vmtk.vmtkbranchclipper',
    'vmtk.vmtkbranchextractor',
    'vmtk.vmtkbranchgeometry',
    'vmtk.vmtkcenterlineimage',
    'vmtk.vmtkbranchmapping',
    'vmtk.vmtkbranchmetrics',
    'vmtk.vmtkbranchpatching',
    'vmtk.vmtkbranchsections',
    'vmtk.vmtkcenterlineattributes',
    'vmtk.vmtkcenterlinegeometry',
    'vmtk.vmtkcenterlineinterpolation',
    'vmtk.vmtkcenterlinelabeler',
    'vmtk.vmtkcenterlinemerge',
    'vmtk.vmtkcenterlinemodeller',
    'vmtk.vmtkcenterlineoffsetattributes',
    'vmtk.vmtkcenterlineresampling',
    'vmtk.vmtkcenterlines',
    'vmtk.vmtkcenterlinestonumpy',
    'vmtk.vmtkcenterlinesections',
    'vmtk.vmtkcenterlinesmoothing',
    'vmtk.vmtkcenterlinesnetwork',
    'vmtk.vmtkcenterlineviewer',
    'vmtk.vmtkdelaunayvoronoi',
    'vmtk.vmtkdistancetocenterlines',
    'vmtk.vmtkendpointextractor',
    'vmtk.vmtkflowextensions',
    'vmtk.vmtkicpregistration',
    'vmtk.vmtkimagebinarize',
    'vmtk.vmtkimagecast',
    'vmtk.vmtkimagecompose',
    'vmtk.vmtkimagecurvedmpr',
    'vmtk.vmtkimagefeaturecorrection',
    'vmtk.vmtkimagefeatures',
    'vmtk.vmtkimageinitialization',
    'vmtk.vmtkimagemipviewer',
    'vmtk.vmtkimagemorphology',
    'vmtk.vmtkimagenormalize',
    'vmtk.vmtkimageobjectenhancement',
    'vmtk.vmtkimageotsuthresholds',
    'vmtk.vmtkimagereader',
    'vmtk.vmtkimagereslice',
    'vmtk.vmtkimageseeder',
    'vmtk.vmtkimageshiftscale',
    'vmtk.vmtkimagesmoothing',
    'vmtk.vmtkimagetonumpy',
    'vmtk.vmtkimageviewer',
    'vmtk.vmtkimagevesselenhancement',
    'vmtk.vmtkimagevoipainter',
    'vmtk.vmtkimagevoiselector',
    'vmtk.vmtkimagevolumeviewer',
    'vmtk.vmtkimagewriter',
    'vmtk.vmtklevelsetsegmentation',
    'vmtk.vmtklineartoquadratic',
    'vmtk.vmtklineresampling',
    'vmtk.vmtklocalgeometry',
    'vmtk.vmtkmarchingcubes',
    'vmtk.vmtkmesharrayoperation',
    'vmtk.vmtkmeshboundaryinspector',
    'vmtk.vmtkmeshbranchclipper',
    'vmtk.vmtkmeshclipper',
    'vmtk.vmtkmeshconnectivity',
    'vmtk.vmtkmeshcutter',
    'vmtk.vmtkmeshdatareader',
    'vmtk.vmtkmeshextractpointdata',
    'vmtk.vmtkmeshlambda2',
    'vmtk.vmtkmeshlinearize',
    'vmtk.vmtkmeshgenerator',
    'vmtk.vmtkmeshmergetimesteps',
    'vmtk.vmtkmeshpolyballevaluation',
    'vmtk.vmtkmeshprojection',
    'vmtk.vmtkmeshreader',
    'vmtk.vmtkmeshscaling',
    'vmtk.vmtkmeshtetrahedralize',
    'vmtk.vmtkmeshtonumpy',
    'vmtk.vmtkmeshtosurface',
    'vmtk.vmtkmeshtransform',
    'vmtk.vmtkmeshtransformtoras',
    'vmtk.vmtkmeshvectorfromcomponents',
    'vmtk.vmtkmeshviewer',
    'vmtk.vmtkmeshvolume',
    'vmtk.vmtkmeshvorticityhelicity',
    'vmtk.vmtkmeshwallshearrate',
    'vmtk.vmtkmeshwriter',
    'vmtk.vmtknetworkeditor',
    'vmtk.vmtknetworkextraction',
    'vmtk.vmtknetworkwriter',
    'vmtk.vmtknumpyreader',
    'vmtk.vmtknumpytocenterlines',
    'vmtk.vmtknumpytoimage',
    'vmtk.vmtknumpytomesh',
    'vmtk.vmtknumpytosurface',
    'vmtk.vmtknumpywriter',
    'vmtk.vmtkparticletracer',
    'vmtk.vmtkpathlineanimator',
    'vmtk.vmtkpointsplitextractor',
    'vmtk.vmtkpointtransform',
    'vmtk.vmtkpolyballmodeller',
    'vmtk.vmtkpotentialfit',
    'vmtk.vmtkpythonscript',
    'vmtk.vmtkrenderer',
    'vmtk.vmtkrendertoimage',
    'vmtk.vmtkrbfinterpolation',
    'vmtk.vmtksurfaceappend',
    'vmtk.vmtksurfacearraysmoothing',
    'vmtk.vmtksurfacearrayoperation',
    'vmtk.vmtksurfacebooleanoperation',
    'vmtk.vmtksurfacecapper',
    'vmtk.vmtksurfacecelldatatopointdata',
    'vmtk.vmtksurfacecenterlineprojection',
    'vmtk.vmtksurfaceclipper',
    'vmtk.vmtksurfacecliploop',
    'vmtk.vmtksurfaceconnectivity',
    'vmtk.vmtksurfaceconnectivityselector',
    'vmtk.vmtksurfacecurvature',
    'vmtk.vmtksurfacedecimation',
    'vmtk.vmtksurfacedistance',
    'vmtk.vmtksurfaceendclipper',
    'vmtk.vmtksurfacekiteremoval',
    'vmtk.vmtksurfaceloopextraction',
    'vmtk.vmtksurfacemassproperties',
    'vmtk.vmtksurfacemodeller',
    'vmtk.vmtksurfacenormals',
    'vmtk.vmtksurfacepointdatatocelldata',
    'vmtk.vmtksurfacepolyballevaluation',
    'vmtk.vmtksurfaceprojection',
    'vmtk.vmtksurfacereader',
    'vmtk.vmtksurfacereferencesystemtransform',
    'vmtk.vmtksurfaceregiondrawing',
    'vmtk.vmtksurfaceremeshing',
    'vmtk.vmtksurfacescaling',
    'vmtk.vmtksurfacesmoothing',
    'vmtk.vmtksurfacesubdivision',
    'vmtk.vmtksurfacetobinaryimage',
    'vmtk.vmtksurfacetonumpy',
    'vmtk.vmtksurfacetransform',
    'vmtk.vmtksurfacetransforminteractive',
    'vmtk.vmtksurfacetransformtoras',
    'vmtk.vmtksurfacetriangle',
    'vmtk.vmtksurfacetomesh',
    'vmtk.vmtksurfaceviewer',
    'vmtk.vmtksurfacewriter',
    'vmtk.vmtksurfmesh',
    'vmtk.vmtktetgen',
    'vmtk.vmtktetringenerator'
    ]

for item in __all__:
    print(item)
    exec('from '+item+' import *')