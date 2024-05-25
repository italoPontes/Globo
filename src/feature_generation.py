import pandas as pd

time_feature = "tempo_modalidades"  # tempo_total ou tempo_modalidades
sport_features = ['futebol', 'futebol_intenacional', 'futebol_olimpico',
                  'blog_cartola', 'atletismo', 'ginastica', 'judo',
                  'natacao', 'basquete', 'handebol', 'volei', 'tenis',
                  'canoagem', 'saltos_ornamentais', 'home', 'home_olimpiadas']
new_features = ["tempo_medio_diario", "tempo_medio_visita",
                "tempo_medio_pagina", "pagina_por_visita", "pagina_por_dia",
                "visitas_por_dia", "quantidade_modalidades", "top_tempo"]
sport_features_perc = [f"{feature}_perc" for feature in sport_features]


def get_sport_features_perc(df: pd.DataFrame = []) -> pd.DataFrame:
    """
    Calcula o tempo total das modalidades e a porcentagem de tempo de cada
    modalidade em relação ao tempo total.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados das modalidades esportivas.

    Retorna:
    pd.DataFrame: DataFrame com colunas adicionais para o tempo total das
    modalidades e as porcentagens de tempo de cada modalidade.
    """
    df[time_feature] = df[sport_features].sum(axis=1)

    for feature_name in sport_features:
        new_feature = f"{feature_name}_perc"
        df[new_feature] = df[feature_name]/df[time_feature]

    return df


def get_time_based_features(df: pd.DataFrame = []) -> pd.DataFrame:
    """
    Calcula métricas baseadas no tempo para cada entrada no DataFrame.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados de tempo e outras métricas
    relevantes como dias, visitas e visualizações de páginas.

    Retorna:
    pd.DataFrame: DataFrame com colunas adicionais para o tempo médio diário,
    tempo médio por visita e tempo médio por página.
    """
    df["tempo_medio_diario"] = df[time_feature] / df["dias"]
    df["tempo_medio_visita"] = df[time_feature] / df["visitas"]
    df["tempo_medio_pagina"] = df[time_feature] / df["pviews"]
    return df


def get_visitas(df: pd.DataFrame = []) -> pd.DataFrame:
    """
    Calcula métricas de visitas para cada entrada no DataFrame.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados de visualizações de páginas
    (pviews), visitas e dias.

    Retorna:
    pd.DataFrame: DataFrame com colunas adicionais para páginas por visita,
    páginas por dia e visitas por dia.
    """
    df["pagina_por_visita"] = df["pviews"]/df["visitas"]
    df["pagina_por_dia"] = df["pviews"]/df["dias"]
    df["visitas_por_dia"] = df["visitas"]/df["dias"]

    return df


def get_modalidades(df: pd.DataFrame = []) -> pd.DataFrame:
    """
    Calcula a quantidade de modalidades diferentes de zero e o tempo máximo
    de modalidades para cada entrada no DataFrame.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo as porcentagens de tempo de cada
    modalidade esportiva.

    Retorna:
    pd.DataFrame: DataFrame com colunas adicionais para a quantidade de
    modalidades diferentes de zero e o tempo máximo das modalidades.
    """
    df["quantidade_modalidades"] = (df[sport_features_perc] != 0).sum(axis=1)
    df["top_tempo"] = df[sport_features_perc].max(axis=1)

    return df


def get_new_features(df: pd.DataFrame = []) -> pd.DataFrame:
    """
    Adiciona novas características derivadas ao DataFrame.

    Esta função aplica uma série de transformações ao DataFrame de entrada
    para calcular novas características baseadas em dados esportivos, tempo,
    visitas e modalidades.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados originais.

    Retorna:
    pd.DataFrame: DataFrame com colunas adicionais contendo as novas
    características calculadas.
    """
    df = get_sport_features_perc(df)
    df = get_time_based_features(df)
    df = get_visitas(df)
    df = get_modalidades(df)

    return df
