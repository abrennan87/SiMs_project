ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'

      INCLUDE 'model_functions.inc'
      GC_20 = (MDL_CKM1X1*MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_21 = (MDL_CKM1X2*MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_23 = (MDL_CKM2X1*MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_24 = (MDL_CKM2X2*MDL_EE*MDL_COMPLEXI)/(MDL_SW*MDL_SQRT__2)
      GC_29 = -(MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_SW)
      GC_30 = (MDL_CW*MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_SW)
      GC_31 = -(MDL_EE*MDL_COMPLEXI*MDL_SW)/(6.000000D+00*MDL_CW)
      GC_50 = (MDL_EE*MDL_COMPLEXI*MDL_CONJG__CKM1X1)/(MDL_SW
     $ *MDL_SQRT__2)
      GC_51 = (MDL_EE*MDL_COMPLEXI*MDL_CONJG__CKM1X2)/(MDL_SW
     $ *MDL_SQRT__2)
      GC_53 = (MDL_EE*MDL_COMPLEXI*MDL_CONJG__CKM2X1)/(MDL_SW
     $ *MDL_SQRT__2)
      GC_54 = (MDL_EE*MDL_COMPLEXI*MDL_CONJG__CKM2X2)/(MDL_SW
     $ *MDL_SQRT__2)
      GC_11 = MDL_COMPLEXI*MDL_GXIC
      GC_12 = MDL_COMPLEXI*MDL_GXICHI
      GC_13 = MDL_COMPLEXI*MDL_GXID
      GC_14 = MDL_COMPLEXI*MDL_GXIS
      GC_16 = MDL_COMPLEXI*MDL_GXIU
      END
