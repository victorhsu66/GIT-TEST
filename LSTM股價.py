{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "LSTM股價.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNatEhRkhKfUUyvtNYkWKlm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "2e73118963d84ed1ae1e73746194a101": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "state": {
            "_view_name": "HBoxView",
            "_dom_classes": [],
            "_model_name": "HBoxModel",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.5.0",
            "box_style": "",
            "layout": "IPY_MODEL_5c2e993d7cbb43d99a60c2f27b1386a1",
            "_model_module": "@jupyter-widgets/controls",
            "children": [
              "IPY_MODEL_30f93c6945d74d08acb875686ebf09fb",
              "IPY_MODEL_8ac7799593204cdab019b47484022bc1"
            ]
          }
        },
        "5c2e993d7cbb43d99a60c2f27b1386a1": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "30f93c6945d74d08acb875686ebf09fb": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatProgressModel",
          "state": {
            "_view_name": "ProgressView",
            "style": "IPY_MODEL_00114325c91d4a289206c38cb80697e1",
            "_dom_classes": [],
            "description": "100%",
            "_model_name": "FloatProgressModel",
            "bar_style": "success",
            "max": 2605,
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "value": 2605,
            "_view_count": null,
            "_view_module_version": "1.5.0",
            "orientation": "horizontal",
            "min": 0,
            "description_tooltip": null,
            "_model_module": "@jupyter-widgets/controls",
            "layout": "IPY_MODEL_f9acd0d6ce0741d0bfb92a7b28f5efce"
          }
        },
        "8ac7799593204cdab019b47484022bc1": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "state": {
            "_view_name": "HTMLView",
            "style": "IPY_MODEL_ec76e10a516947118d36454031334569",
            "_dom_classes": [],
            "description": "",
            "_model_name": "HTMLModel",
            "placeholder": "​",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "value": " 2605/2605 [00:00&lt;00:00, 3059.85it/s]",
            "_view_count": null,
            "_view_module_version": "1.5.0",
            "description_tooltip": null,
            "_model_module": "@jupyter-widgets/controls",
            "layout": "IPY_MODEL_ed89300bb61744ec80043d52148e3abf"
          }
        },
        "00114325c91d4a289206c38cb80697e1": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ProgressStyleModel",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ProgressStyleModel",
            "description_width": "initial",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.2.0",
            "bar_color": null,
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "f9acd0d6ce0741d0bfb92a7b28f5efce": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "ec76e10a516947118d36454031334569": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "DescriptionStyleModel",
            "description_width": "",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "ed89300bb61744ec80043d52148e3abf": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        }
      }
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/victorhsu66/GIT-TEST/blob/main/LSTM%E8%82%A1%E5%83%B9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1LuozV5vGn_v",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 232
        },
        "outputId": "cc710e1d-67cd-4169-d6bd-df9589a19bba"
      },
      "source": [
        "#http://moocs.nccu.edu.tw/mobile/media/17888\n",
        "import pandas_datareader.data as web\n",
        "import datetime\n",
        "df=web.DataReader(\"0050.TW\" , \"yahoo\" , start=\"2009-1-1\", end=\"2019-8-1\")\n",
        "df.head()\n",
        "# p=df[\"Adj Close\"]\n",
        "# p.head()\n",
        "# p.plot()\n",
        "# r=p.diff()/p\n",
        "# r[-100:].plot()\n",
        "# p.plot()\n",
        "# p.rolling(window=20).mean().plot()#20天移動平均\n",
        "# p.rolling(window=60).mean().plot()#60天移動平均"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>High</th>\n",
              "      <th>Low</th>\n",
              "      <th>Open</th>\n",
              "      <th>Close</th>\n",
              "      <th>Volume</th>\n",
              "      <th>Adj Close</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2009-01-02</th>\n",
              "      <td>32.869999</td>\n",
              "      <td>32.869999</td>\n",
              "      <td>32.869999</td>\n",
              "      <td>32.869999</td>\n",
              "      <td>0.0</td>\n",
              "      <td>32.869999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2009-01-05</th>\n",
              "      <td>36.590000</td>\n",
              "      <td>30.570000</td>\n",
              "      <td>35.169998</td>\n",
              "      <td>36.590000</td>\n",
              "      <td>26338.0</td>\n",
              "      <td>36.590000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2009-01-06</th>\n",
              "      <td>36.590000</td>\n",
              "      <td>33.930000</td>\n",
              "      <td>36.590000</td>\n",
              "      <td>36.570000</td>\n",
              "      <td>24377.0</td>\n",
              "      <td>36.570000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2009-01-07</th>\n",
              "      <td>34.869999</td>\n",
              "      <td>32.209999</td>\n",
              "      <td>34.700001</td>\n",
              "      <td>32.209999</td>\n",
              "      <td>16672.0</td>\n",
              "      <td>32.209999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2009-01-08</th>\n",
              "      <td>33.810001</td>\n",
              "      <td>30.160000</td>\n",
              "      <td>33.599998</td>\n",
              "      <td>30.160000</td>\n",
              "      <td>31357.0</td>\n",
              "      <td>30.160000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                 High        Low       Open      Close   Volume  Adj Close\n",
              "Date                                                                      \n",
              "2009-01-02  32.869999  32.869999  32.869999  32.869999      0.0  32.869999\n",
              "2009-01-05  36.590000  30.570000  35.169998  36.590000  26338.0  36.590000\n",
              "2009-01-06  36.590000  33.930000  36.590000  36.570000  24377.0  36.570000\n",
              "2009-01-07  34.869999  32.209999  34.700001  32.209999  16672.0  32.209999\n",
              "2009-01-08  33.810001  30.160000  33.599998  30.160000  31357.0  30.160000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 232
        },
        "id": "98iw1qMD8xM-",
        "outputId": "be5da8ad-12ee-4b3f-987b-5e28dc0d6dbf"
      },
      "source": [
        "#https://skywalker0803r.medium.com/keras-%E5%AF%A6%E4%BD%9Clstm%E8%82%A1%E5%83%B9%E6%BC%B2%E8%B7%8C%E9%A0%90%E6%B8%AC-b0036f104d3b\n",
        "df=df[['Open','Low','High','Volume','Close']]\n",
        "df.tail()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Open</th>\n",
              "      <th>Low</th>\n",
              "      <th>High</th>\n",
              "      <th>Volume</th>\n",
              "      <th>Close</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2019-07-29</th>\n",
              "      <td>83.099998</td>\n",
              "      <td>83.050003</td>\n",
              "      <td>83.449997</td>\n",
              "      <td>3042246.0</td>\n",
              "      <td>83.449997</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-07-30</th>\n",
              "      <td>83.599998</td>\n",
              "      <td>83.199997</td>\n",
              "      <td>83.699997</td>\n",
              "      <td>2083374.0</td>\n",
              "      <td>83.199997</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-07-31</th>\n",
              "      <td>83.150002</td>\n",
              "      <td>82.449997</td>\n",
              "      <td>83.150002</td>\n",
              "      <td>3119262.0</td>\n",
              "      <td>82.800003</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-08-01</th>\n",
              "      <td>82.199997</td>\n",
              "      <td>82.099998</td>\n",
              "      <td>82.550003</td>\n",
              "      <td>5042943.0</td>\n",
              "      <td>82.300003</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-08-02</th>\n",
              "      <td>81.050003</td>\n",
              "      <td>80.599998</td>\n",
              "      <td>81.199997</td>\n",
              "      <td>16846402.0</td>\n",
              "      <td>80.949997</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                 Open        Low       High      Volume      Close\n",
              "Date                                                              \n",
              "2019-07-29  83.099998  83.050003  83.449997   3042246.0  83.449997\n",
              "2019-07-30  83.599998  83.199997  83.699997   2083374.0  83.199997\n",
              "2019-07-31  83.150002  82.449997  83.150002   3119262.0  82.800003\n",
              "2019-08-01  82.199997  82.099998  82.550003   5042943.0  82.300003\n",
              "2019-08-02  81.050003  80.599998  81.199997  16846402.0  80.949997"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 286
        },
        "id": "7gUZeaXU-aX1",
        "outputId": "18e240df-e458-4853-aad5-9b90f2b07c70"
      },
      "source": [
        "df.Close.plot()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f7a2d0c51d0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 232
        },
        "id": "E1czBMeV-5v6",
        "outputId": "7f321295-b7e2-4811-afe7-644a68f78630"
      },
      "source": [
        "n=1\n",
        "df['return']=df['Close'].shift(-n) - df['Close']\n",
        "df.tail()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Open</th>\n",
              "      <th>Low</th>\n",
              "      <th>High</th>\n",
              "      <th>Volume</th>\n",
              "      <th>Close</th>\n",
              "      <th>return</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2019-07-29</th>\n",
              "      <td>83.099998</td>\n",
              "      <td>83.050003</td>\n",
              "      <td>83.449997</td>\n",
              "      <td>3042246.0</td>\n",
              "      <td>83.449997</td>\n",
              "      <td>-0.250000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-07-30</th>\n",
              "      <td>83.599998</td>\n",
              "      <td>83.199997</td>\n",
              "      <td>83.699997</td>\n",
              "      <td>2083374.0</td>\n",
              "      <td>83.199997</td>\n",
              "      <td>-0.399994</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-07-31</th>\n",
              "      <td>83.150002</td>\n",
              "      <td>82.449997</td>\n",
              "      <td>83.150002</td>\n",
              "      <td>3119262.0</td>\n",
              "      <td>82.800003</td>\n",
              "      <td>-0.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-08-01</th>\n",
              "      <td>82.199997</td>\n",
              "      <td>82.099998</td>\n",
              "      <td>82.550003</td>\n",
              "      <td>5042943.0</td>\n",
              "      <td>82.300003</td>\n",
              "      <td>-1.350006</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-08-02</th>\n",
              "      <td>81.050003</td>\n",
              "      <td>80.599998</td>\n",
              "      <td>81.199997</td>\n",
              "      <td>16846402.0</td>\n",
              "      <td>80.949997</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                 Open        Low       High      Volume      Close    return\n",
              "Date                                                                        \n",
              "2019-07-29  83.099998  83.050003  83.449997   3042246.0  83.449997 -0.250000\n",
              "2019-07-30  83.599998  83.199997  83.699997   2083374.0  83.199997 -0.399994\n",
              "2019-07-31  83.150002  82.449997  83.150002   3119262.0  82.800003 -0.500000\n",
              "2019-08-01  82.199997  82.099998  82.550003   5042943.0  82.300003 -1.350006\n",
              "2019-08-02  81.050003  80.599998  81.199997  16846402.0  80.949997       NaN"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aFPolwsLAvBY"
      },
      "source": [
        "預處理,但return保持原本的值即可\n",
        "\n",
        "preprocessing\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 232
        },
        "id": "8wzSIstW_vlu",
        "outputId": "512a245c-16ee-4dc0-ed24-c3887786d817"
      },
      "source": [
        "import pandas as pd\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "ss=StandardScaler()\n",
        "df_scaled = ss.fit_transform(df)\n",
        "df_scaled = pd.DataFrame(df_scaled,index=df.index,columns=df.columns)\n",
        "df_scaled['return'] = df['return']\n",
        "df_scaled.tail()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Open</th>\n",
              "      <th>Low</th>\n",
              "      <th>High</th>\n",
              "      <th>Volume</th>\n",
              "      <th>Close</th>\n",
              "      <th>return</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2019-07-29</th>\n",
              "      <td>1.650347</td>\n",
              "      <td>1.677197</td>\n",
              "      <td>1.676285</td>\n",
              "      <td>-0.463494</td>\n",
              "      <td>1.693094</td>\n",
              "      <td>-0.250000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-07-30</th>\n",
              "      <td>1.691477</td>\n",
              "      <td>1.689557</td>\n",
              "      <td>1.697197</td>\n",
              "      <td>-0.591215</td>\n",
              "      <td>1.672314</td>\n",
              "      <td>-0.399994</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-07-31</th>\n",
              "      <td>1.654461</td>\n",
              "      <td>1.627751</td>\n",
              "      <td>1.651190</td>\n",
              "      <td>-0.453236</td>\n",
              "      <td>1.639066</td>\n",
              "      <td>-0.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-08-01</th>\n",
              "      <td>1.576314</td>\n",
              "      <td>1.598909</td>\n",
              "      <td>1.601000</td>\n",
              "      <td>-0.197004</td>\n",
              "      <td>1.597504</td>\n",
              "      <td>-1.350006</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-08-02</th>\n",
              "      <td>1.481717</td>\n",
              "      <td>1.475296</td>\n",
              "      <td>1.488071</td>\n",
              "      <td>1.375204</td>\n",
              "      <td>1.485289</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                Open       Low      High    Volume     Close    return\n",
              "Date                                                                  \n",
              "2019-07-29  1.650347  1.677197  1.676285 -0.463494  1.693094 -0.250000\n",
              "2019-07-30  1.691477  1.689557  1.697197 -0.591215  1.672314 -0.399994\n",
              "2019-07-31  1.654461  1.627751  1.651190 -0.453236  1.639066 -0.500000\n",
              "2019-08-01  1.576314  1.598909  1.601000 -0.197004  1.597504 -1.350006\n",
              "2019-08-02  1.481717  1.475296  1.488071  1.375204  1.485289       NaN"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9bVlQoamDYjM"
      },
      "source": [
        "再來製作X跟Y.\n",
        "\n",
        "make X,y for LSTM model\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 138,
          "referenced_widgets": [
            "2e73118963d84ed1ae1e73746194a101",
            "5c2e993d7cbb43d99a60c2f27b1386a1",
            "30f93c6945d74d08acb875686ebf09fb",
            "8ac7799593204cdab019b47484022bc1",
            "00114325c91d4a289206c38cb80697e1",
            "f9acd0d6ce0741d0bfb92a7b28f5efce",
            "ec76e10a516947118d36454031334569",
            "ed89300bb61744ec80043d52148e3abf"
          ]
        },
        "id": "dLyV83QEDj-R",
        "outputId": "1b1e23c6-f642-40f5-b7e1-38c9c51bde60"
      },
      "source": [
        "import tqdm\n",
        "\n",
        "n=3\n",
        "feature_names = list(df_scaled.drop('return',axis=1).columns)\n",
        "x= []\n",
        "y= []\n",
        "indexes=[]\n",
        "df_scaled_x = df_scaled[feature_names]\n",
        "\n",
        "for i in tqdm.tqdm_notebook(range(0,len(df_scaled)-n)):\n",
        "  x.append(df_scaled_x.iloc[i:i+n].values)\n",
        "  y.append(df_scaled['return'].iloc[i+n-1])\n",
        "  indexes.append(df_scaled.index[i+n-1])\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:10: TqdmDeprecationWarning: This function will be removed in tqdm==5.0.0\n",
            "Please use `tqdm.notebook.tqdm` instead of `tqdm.tqdm_notebook`\n",
            "  # Remove the CWD from sys.path while we load stuff.\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "2e73118963d84ed1ae1e73746194a101",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "HBox(children=(FloatProgress(value=0.0, max=2605.0), HTML(value='')))"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NC9H9wdlHe_M"
      },
      "source": [
        "這裡是一個比較關鍵的部份,這裡每一筆test_case都是n天m維的X,配上一個y\n",
        "\n",
        "為什麼是n天m維的X呢?,是為了要利用LSTM的特性來做的資料轉換.\n",
        "\n",
        "例如輸入三天的”開高低收量”,這樣的資料就是一個3天5維的X\n",
        "\n",
        "其shape=(3,5),而他的y就是第三天的return.\n",
        "\n",
        "這樣一筆test_case就是X.shape=(3,5) y.shape=(1)\n",
        "\n",
        "而用一個for迴圈對df做滑動之後就可以得到好幾筆test_case\n",
        "\n",
        "最終shape是"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hzhdr-ruILm-",
        "outputId": "8310f77d-f32c-41ed-d587-bbea4a71f77c"
      },
      "source": [
        "import numpy as np\n",
        "x=np.array(x)\n",
        "y=np.array(y)\n",
        "print(x.shape)\n",
        "print(y.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(2605, 3, 5)\n",
            "(2605,)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3TP4Yg2kI3B7"
      },
      "source": [
        "**再來就是建立我的LSTM MODEL**\n",
        "\n",
        "神經網路Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sNODKuXhJUFG",
        "outputId": "49ce6a10-380f-437a-bb4e-86dc606551f8"
      },
      "source": [
        "import keras\n",
        "\n",
        "model = keras.models.Sequential() #顺序模型:是多个网络层的线性堆叠。\n",
        "model.add(keras.layers.LSTM(100,return_sequences=True, input_shape=x[0].shape))\n",
        "model.add(keras.layers.LSTM(100))\n",
        "model.add(keras.layers.Dense(8))\n",
        "model.add(keras.layers.Dense(1,kernel_initializer=\"uniform\",activation='linear'))\n",
        "\n",
        "adam = keras.optimizers.Adam(0.0006)\n",
        "\n",
        "model.compile(optimizer=adam, loss=\"binary_crossentropy\", metrics=['accuracy'])\n",
        "\n",
        "model.summary()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Model: \"sequential\"\n",
            "_________________________________________________________________\n",
            "Layer (type)                 Output Shape              Param #   \n",
            "=================================================================\n",
            "lstm (LSTM)                  (None, 3, 100)            42400     \n",
            "_________________________________________________________________\n",
            "lstm_1 (LSTM)                (None, 100)               80400     \n",
            "_________________________________________________________________\n",
            "dense (Dense)                (None, 8)                 808       \n",
            "_________________________________________________________________\n",
            "dense_1 (Dense)              (None, 1)                 9         \n",
            "=================================================================\n",
            "Total params: 123,617\n",
            "Trainable params: 123,617\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EW4-iZ2lMlRq"
      },
      "source": [
        "這裡使用兩層LSTM,一個比較怪的部份是為何loss_function不是用mse\n",
        "\n",
        "return應該是一個數值,算是回歸問題吧?\n",
        "\n",
        "這是因為預測股價確切點數是很困難的,不如預測他漲或跌就好.\n",
        "\n",
        "**神經網路訓練**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JUg7OvA3Jkep",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 237
        },
        "outputId": "d463cccb-e91d-4aa2-fa7a-bd4956998d93"
      },
      "source": [
        "# from datetime import datetime\n",
        "import datetime\n",
        "x_train = x(indexes < datetime.datetime(2016, 1, 1))\n",
        "y_train = y[indexes < datetime(2016, 1, 1)]\n",
        "\n",
        "get_best_model = keras.callbacks.ModelCheckpoint(\"lstm.mdl\",monitor=\"val_acc\")\n",
        "\n",
        "history = model.fit(\n",
        "    x_train,\n",
        "    y_train > 1,\n",
        "    batch_size=1000,\n",
        "    epochs=50,\n",
        "    validation_split=0.2,\n",
        "    callbacks=[get_best_model])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-21-221aa64d6e55>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# from datetime import datetime\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mx_train\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mindexes\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdatetime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2016\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0my_train\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mindexes\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2016\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: '<' not supported between instances of 'list' and 'datetime.datetime'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "86_tOwRrZ0l_",
        "outputId": "a99453c9-9626-497b-b1d2-05ebe2dc59bd"
      },
      "source": [
        "import datetime\n",
        "\n",
        "dti = pd.to_datetime(['1/1/2018', np.datetime64('2018-01-01'),\n",
        "                          datetime.datetime(2018, 1, 1)])\n",
        "   \n",
        "\n",
        "dti"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DatetimeIndex(['2018-01-01', '2018-01-01', '2018-01-01'], dtype='datetime64[ns]', freq=None)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    }
  ]
}