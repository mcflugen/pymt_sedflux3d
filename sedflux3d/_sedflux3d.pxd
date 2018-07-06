


cdef extern from "sedflux3d/bmi_sedflux3d.h":
    ctypedef struct BMI_Model:
        pass

    BMI_Model* register_bmi_sedflux3d(BMI_Model *model)


