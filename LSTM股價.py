{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "LSTM股價.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNatEhRkhKfUUyvtNYkWKlm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "id": "1LuozV5vGn_v"
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
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "98iw1qMD8xM-"
      },
      "source": [
        "#https://skywalker0803r.medium.com/keras-%E5%AF%A6%E4%BD%9Clstm%E8%82%A1%E5%83%B9%E6%BC%B2%E8%B7%8C%E9%A0%90%E6%B8%AC-b0036f104d3b\n",
        "df=df[['Open','Low','High','Volume','Close']]\n",
        "df.tail()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7gUZeaXU-aX1"
      },
      "source": [
        "df.Close.plot()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "E1czBMeV-5v6"
      },
      "source": [
        "n=1\n",
        "df['return']=df['Close'].shift(-n) - df['Close']\n",
        "df.tail()"
      ],
      "execution_count": null,
      "outputs": []
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
        "id": "8wzSIstW_vlu"
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
      "outputs": []
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
        "id": "dLyV83QEDj-R"
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
      "outputs": []
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
        "id": "sNODKuXhJUFG"
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
      "outputs": []
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
        "id": "JUg7OvA3Jkep"
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
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "86_tOwRrZ0l_"
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
      "outputs": []
    }
  ]
}