import matplotlib.pyplot as plt
import numpy as np

plt.rc("font", **{"family": "serif", "serif": ["Computer Modern"]})
plt.rc("text", usetex=True)

g_fontsize_legend = 10
g_fontsize_xlabel = 30
g_fontsize_ylabel = 30
g_fontsize_xyticklabels = 16

g_color_1 = "#5e3c99"
g_color_2 = "#e66101"

g_xlim = [12.0,15.0]

g_xlabel = "log $N_{C_{IV}} (cm^{-2})$"
g_ylabel = "log $f_{C_{IV}}$"

g_file_dpi = 200
g_plot_dpi = 75

def main():

    sim1 = np.genfromtxt("c4_cddf_18_MDW_no_4.8.txt", names=True)
    sim2 = np.genfromtxt("c4_cddf_18_MDW_mol_4.8.txt", names=True)
    sim3 = np.genfromtxt("c4_cddf_18_EDW_no_4.8.txt", names=True)
    sim4 = np.genfromtxt("c4_cddf_18_EDW_mol_4.8.txt", names=True)
    sim5 = np.genfromtxt("c4_cddf_25_4.8.txt", names=True)
    sim6 = np.genfromtxt("c4_cddf_12_4.8.txt", names=True)
    obs = np.genfromtxt("obs_dodorico_civ_cddf_z_4.8.txt", names=True)

    sim_dummy_1 = sim1["n_left"]
    sim_dummy_2 = sim1["n_right"]
    sim_xdata = sim1["n_mid"]
    sim_dummy_3 = sim1["n"]
    sim_ydata = sim1["fn"]

    sim_dummy_1_2 = sim2["n_left"]
    sim_dummy_2_2 = sim2["n_right"]
    sim_xdata_2 = sim2["n_mid"]
    sim_dummy_3_2 = sim2["n"]
    sim_ydata_2 = sim2["fn"]

    sim_dummy_1_3 = sim3["n_left"]
    sim_dummy_2_3 = sim3["n_right"]
    sim_xdata_3 = sim3["n_mid"]
    sim_dummy_3_3 = sim3["n"]
    sim_ydata_3 = sim3["fn"]

    sim_dummy_1_4 = sim4["n_left"]
    sim_dummy_2_4 = sim4["n_right"]
    sim_xdata_4 = sim4["n_mid"]
    sim_dummy_3_4 = sim4["n"]
    sim_ydata_4 = sim4["fn"]

    sim_dummy_1_5 = sim5["n_left"]
    sim_dummy_2_5 = sim5["n_right"]
    sim_xdata_5 = sim5["n_mid"]
    sim_dummy_3_5 = sim5["n"]
    sim_ydata_5 = sim5["fn"]

    sim_dummy_1_6 = sim6["n_left"]
    sim_dummy_2_6 = sim6["n_right"]
    sim_xdata_6 = sim6["n_mid"]
    sim_dummy_3_6 = sim6["n"]
    sim_ydata_6 = sim6["fn"]

    obs_xdata = obs["logN"]
    obs_ydata = obs["logf"]
    obs_ydata_err_1 = obs["down"]
    obs_ydata_err_2 = obs["up"]
    obs_xdata_err_1 = obs["left"]
    obs_xdata_err_2 = obs["right"]

    # Create figure.
    fig = plt.figure(figsize=(8, 8))

    # Add axes to figure.
    ax = fig.add_subplot(1, 1, 1)

    # Configure the axes.
    #ax.set_yscale("log")
    ax.set_xlim(g_xlim)
    ax.tick_params(labelsize=g_fontsize_xyticklabels)
    ax.set_xlabel(g_xlabel, fontsize=g_fontsize_xlabel)
    ax.set_ylabel(g_ylabel, fontsize=g_fontsize_ylabel)

    fit = np.polyfit(sim_xdata,sim_ydata,1)
    fit_fn = np.poly1d(fit) 
    fit_2 = np.polyfit(sim_xdata_2,sim_ydata_2,1)
    fit_fn_2 = np.poly1d(fit_2)
    fit_3 = np.polyfit(sim_xdata_3,sim_ydata_3,1)
    fit_fn_3 = np.poly1d(fit_3)
    fit_4 = np.polyfit(sim_xdata_4,sim_ydata_4,1)
    fit_fn_4 = np.poly1d(fit_4)
    fit_5 = np.polyfit(sim_xdata_5,sim_ydata_5,1)
    fit_fn_5 = np.poly1d(fit_5)
    fit_6 = np.polyfit(sim_xdata_6,sim_ydata_6,1)
    fit_fn_6 = np.poly1d(fit_6)

    # Draw a best-fit straight line and the fittings from Dodorico
    ax.plot(sim_xdata,10.2906-1.75262*sim_xdata, "--k",color='black', linewidth=2.0)
    ax.plot(sim_xdata, 8.5368-1.62*sim_xdata,"-.k",color='black', linewidth=2.0)
    ax.plot(sim_xdata, fit_fn(sim_xdata),'-',color='blue', linewidth=2.0)
    ax.plot(sim_xdata, fit_fn_2(sim_xdata),'-',color='darkred', linewidth=2.0)
    ax.plot(sim_xdata, fit_fn_3(sim_xdata),'-',color='green', linewidth=2.0)
    ax.plot(sim_xdata, fit_fn_4(sim_xdata),'-',color='magenta', linewidth=2.0)
    ax.plot(sim_xdata, fit_fn_6(sim_xdata),'-',color='yellow', linewidth=2.0)
    ax.plot(sim_xdata, fit_fn_5(sim_xdata),'-',color=g_color_1, linewidth=2.0)

    # Plot the data inside the axes.
    #ax.scatter(sim_xdata, sim_ydata, color='black', s=60)
    #ax.scatter(sim_xdata_2, sim_ydata_2, color='violet', s=60)
    #ax.scatter(sim_xdata_3, sim_ydata_3, color='green', s=60)
    #ax.scatter(sim_xdata_4, sim_ydata_4, color='magenta', s=60)
    #ax.scatter(sim_xdata_5, sim_ydata_5, color='grey', s=60)
    #ax.scatter(sim_xdata_6, sim_ydata_6, color=g_color_1, s=60)
    ax.scatter(obs_xdata, obs_ydata, color=g_color_2, s=60)
    # Plot error bars.
    (_, caps, _) = ax.errorbar(obs_xdata, obs_ydata, yerr=[obs_ydata_err_1, obs_ydata_err_2],xerr=[obs_xdata_err_1,obs_xdata_err_2],fmt="None", ecolor=g_color_2, elinewidth=3, capsize=5)

    # Adjust the size and color of the error bar caps.
    for cap in caps:
        cap.set_color(g_color_2)
        cap.set_markeredgewidth(3)

    # Setup legend.
    legend_lines = []
    legend_labels = []
    legend_lines.append(plt.Line2D((0, 0), (0, 0), linewidth=0, color=g_color_2, marker="o", markersize=5, markeredgewidth=1.5, markeredgecolor=g_color_2))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), color='black', linestyle='--', linewidth=2.0, markeredgecolor='black'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), color='black', linestyle='-.', linewidth=2.0, markeredgecolor='black'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), color='blue', linestyle='-', linewidth=2.0, markeredgecolor='blue'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), color='darkred', linestyle='-', linewidth=2.0, markeredgecolor='darkred'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), color='green',linestyle='-', linewidth=2.0, markeredgecolor='green'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), color='magenta',linestyle='-', linewidth=2.0, markeredgecolor='magenta'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), color='yellow',linestyle='-', linewidth=2.0, markeredgecolor='yellow'))
    legend_lines.append(plt.Line2D((0, 0), (0, 0), color=g_color_1, linestyle='-', linewidth=2.0, markeredgecolor=g_color_1))
    legend_labels.append("Obs D\'Odorico 4.35 $< z <$ 5.3")
    legend_labels.append("f(N)$= B N^{-a}$")
    legend_labels.append("f(N)$= f(N_o)(N/N_o)^{-a}$")
    legend_labels.append("Ch 18 512 MDW no mol")
    legend_labels.append("Ch 18 512 MDW mol")
    legend_labels.append("Ch 18 512 EDW no mol")
    legend_labels.append("Ch 18 512 EDW mol")
    legend_labels.append("Ch 12 512 MDW")
    legend_labels.append("Ch 25 512 MDW")

    ax.legend(legend_lines, legend_labels, loc="best", numpoints=1, ncol=1, fontsize=g_fontsize_legend, handlelength=2.0, frameon=False)

    # Save all the above in a file.
    plt.savefig("figure.png", bbox_inches="tight", dpi=g_file_dpi)

    # Show all the above.
    plt.show()


if __name__ == "__main__":
    main()
