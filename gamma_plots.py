import msgpack
import numpy as np
import matplotlib.pyplot as plt
from penetration import PenetrationAnalisys

# Custom decoder for numpy.ndarray
def ndarray_decoder(obj):
    if "__ndarray__" in obj:
        return np.frombuffer(obj["data"], dtype=obj["dtype"]).reshape(obj["shape"])
    return obj


if __name__ == "__main__":
    file_path = f"file_name.msgpack"

    with open(file_path, "rb") as f:
        unpacker = msgpack.Unpacker(f, object_hook=ndarray_decoder, raw=False)
        for obj in unpacker:
            z = obj["z"]
            phi1 = obj["phi1"]
            phi2 = obj["phi2"]
            D =   # Берется то же самое, при котором происходило генерация файла
            PA = PenetrationAnalisys(z, phi1, phi2)


            delta = 0.5*(PA.delta1 + PA.delta2)
            z_new = np.linspace(0, D, 1000)
            phi_a = PA.phi_m*0.5*(1-np.tanh((z_new - PA.z_m) / delta ))
            phi_b = PA.phi_m*0.5*(1+np.tanh((z_new - PA.z_m) / delta ))

            # Для самопроверки или записи в таблицу

            # print(round(PA.phi_m,3))
            # print(round(PA.delta1,1))
            # print(round(PA.delta1,1))
            # print(round(PA.Sigma1, 1))
            # print(round(PA.Sigma1/PA.Sigma2, 1))

            plt.plot((z-PA.z_m)/delta, 4*phi1*phi2 / PA.phi_m**2, marker = "o", linestyle = "none", markersize = 10, color="#FF00FF")
            plt.plot((z_new-PA.z_m) / delta, 4*phi_a*phi_b / PA.phi_m**2, "--", color="black")

        plt.ylabel(r"$4 \cdot \varphi_1(z)\varphi_2(z)/ \varphi_m^2 $", fontsize = 18)
        plt.xlabel("$(z-z_m)/ \delta$", fontsize = 18)
        plt.xlim(-2, 2)
        plt.ylim(0.0, 1.1)
        plt.yticks(fontsize=14)
        # plt.show()
        plt.savefig(f"overlap_func.png", dpi=150, bbox_inches="tight")