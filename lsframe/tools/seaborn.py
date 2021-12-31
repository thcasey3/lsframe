"""
seaborn module, for making a relplot with seaborn
"""
import seaborn as sns


class sea:
    """
    Calls seaborn relplot (https://seaborn.pydata.org/generated/seaborn.relplot.html#seaborn.relplot)

    Args:
        df (pd.DataFrame): df with data to visualize
        kind (str): type of plot (currently only relplot is supported)
        seaborn_args (dict): {'arg': value} for updating seaborn.relplot arguments from default
    Returns:
        seaborn relplot
    """

    def __init__(self, df=None, kind="relplot", seaborn_args={}):

        if kind == "relplot":
            self.plt_relplot(df=df, seaborn_args=seaborn_args)
        else:
            raise ValueError("only relplot is currently supported")

    def plt_relplot(
        self,
        df,
        seaborn_args,
    ):
        sea_args = {
            "theme": "white",
            "hue": None,
            "s": 25,
            "size": None,
            "style": None,
            "row": None,
            "col": None,
            "col_wrap": None,
            "row_order": None,
            "col_order": None,
            "palette": "muted",
            "hue_order": None,
            "hue_norm": None,
            "sizes": (40, 400),
            "size_order": None,
            "size_norm": None,
            "markers": None,
            "dashes": None,
            "style_order": None,
            "legend": "auto",
            "kind": "scatter",
            "height": 5,
            "aspect": 1,
            "alpha": 0.5,
            "facet_kws": None,
            "units": None,
        }
        sea_args.update(seaborn_args)
        sns.set_theme(style=sea_args["theme"])

        sns.relplot(
            data=df,
            x=sea_args["x"],
            y=sea_args["y"],
            hue=sea_args["hue"],
            s=sea_args["s"],
            size=sea_args["size"],
            style=sea_args["style"],
            row=sea_args["row"],
            col=sea_args["col"],
            col_wrap=sea_args["col_wrap"],
            row_order=sea_args["row_order"],
            col_order=sea_args["col_order"],
            palette=sea_args["palette"],
            hue_order=sea_args["hue_order"],
            hue_norm=sea_args["hue_norm"],
            sizes=sea_args["sizes"],
            size_order=sea_args["size_order"],
            size_norm=sea_args["size_norm"],
            markers=sea_args["markers"],
            dashes=sea_args["dashes"],
            style_order=sea_args["style_order"],
            legend="auto",
            kind="scatter",
            height=5,
            aspect=1,
            alpha=sea_args["alpha"],
            facet_kws=sea_args["facet_kws"],
            units=sea_args["units"],
        )
