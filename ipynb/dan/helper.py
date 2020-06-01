import numpy as np
import pandas as pd


def save_obj_by_numpy(filepath, obj):
    np.save(open(filepath, 'wb'), obj)


def load_numpy(filepath):
    return np.load(open(filepath, 'rb'))


def explain_song_list(
    df,
    df_sm,
    df_gr,
    index=None,
    song_ids=None,
):
    """
    df_sm: song_meta dataframe
    df_gr: genre dataframe
    """

    def code2desc(genre_codes):
        return df_gr[
            df_gr.code.isin(genre_codes)
        ].desc.values

    if index is not None:
        song_ids = df.iloc[index].songs

    mask = df_sm.id.isin(song_ids)
    cols = [
        'artist_name_basket',
        'song_gn_dtl_gnr_basket',
        'song_gn_gnr_basket',
        'song_name',
    ]
    tmp = df_sm[mask][cols]
    song_desc = []
    gn_counter = []
    for artist, gn_dtl, gn, name in tmp.values:
        #         gn_total = gn_dtl + gn
        #         print(gn_total)
        gn_dtl = code2desc(gn_dtl)
        gn = code2desc(gn)
        gn_counter += list(gn)
        song_desc.append((artist, gn_dtl, gn, name))

    from collections import Counter
    gn_counter = Counter(gn_counter)

    return pd.DataFrame(song_desc, columns=cols), gn_counter
