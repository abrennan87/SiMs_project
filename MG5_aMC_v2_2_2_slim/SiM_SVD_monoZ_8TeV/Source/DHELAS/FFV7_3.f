C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(3,2,-1)*ProjM(-1,1)
C     
      SUBROUTINE FFV7_3(F1, F2, COUP, M3, W3,V3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 DENOM
      COMPLEX*16 V3(6)
      REAL*8 W3
      COMPLEX*16 TMP0
      REAL*8 P3(0:3)
      REAL*8 M3
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      REAL*8 OM3
      COMPLEX*16 COUP
      OM3 = 0D0
      IF (M3.NE.0D0) OM3=1D0/M3**2
      V3(1) = +F1(1)+F2(1)
      V3(2) = +F1(2)+F2(2)
      P3(0) = -DBLE(V3(1))
      P3(1) = -DBLE(V3(2))
      P3(2) = -DIMAG(V3(2))
      P3(3) = -DIMAG(V3(1))
      TMP0 = (F1(3)*(F2(5)*(P3(0)+P3(3))+F2(6)*(P3(1)+CI*(P3(2))))
     $ +F1(4)*(F2(5)*(P3(1)-CI*(P3(2)))+F2(6)*(P3(0)-P3(3))))
      DENOM = COUP/(P3(0)**2-P3(1)**2-P3(2)**2-P3(3)**2 - M3 * (M3 
     $ -CI* W3))
      V3(3)= DENOM*-CI*(F2(5)*F1(3)+F2(6)*F1(4)-P3(0)*OM3*TMP0)
      V3(4)= DENOM*-CI*(-F2(5)*F1(4)-F2(6)*F1(3)-P3(1)*OM3*TMP0)
      V3(5)= DENOM*-CI*(-CI*(F2(6)*F1(3))+CI*(F2(5)*F1(4))-P3(2)*OM3
     $ *TMP0)
      V3(6)= DENOM*-CI*(F2(6)*F1(4)-F2(5)*F1(3)-P3(3)*OM3*TMP0)
      END


C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(3,2,-1)*ProjM(-1,1)
C     
      SUBROUTINE FFV7_9_3(F1, F2, COUP1, COUP2, M3, W3,V3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 DENOM
      COMPLEX*16 V3(6)
      REAL*8 W3
      REAL*8 P3(0:3)
      REAL*8 M3
      COMPLEX*16 F1(*)
      COMPLEX*16 COUP1
      COMPLEX*16 F2(*)
      COMPLEX*16 COUP2
      REAL*8 OM3
      INTEGER*4 I
      COMPLEX*16 VTMP(6)
      CALL FFV7_3(F1,F2,COUP1,M3,W3,V3)
      CALL FFV9_3(F1,F2,COUP2,M3,W3,VTMP)
      DO I = 3, 6
        V3(I) = V3(I) + VTMP(I)
      ENDDO
      END


