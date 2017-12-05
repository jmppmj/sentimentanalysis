import sqlite3

#Analyzes the sentiment of each title's corresponding group of comments.
#Certain words are defined as indicating positive and negative emotion.
#If a pre-defined positive word is detected, 1 is added to the over finalCount.
#If a pre-defined negative word is detected, -1 is subtracted from the overall finalCount.
#Populates column for corresponding database row with final sentiment number.

def senti1():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 1 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 1;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()

def senti2():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 2 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 2;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()

def senti3():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 3 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 3;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti4():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 4 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 4;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()

def senti5():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 5 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 5;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti6():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 6 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 6;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti7():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 7 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 7;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti8():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 8 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 8;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti9():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 9 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 9;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti10():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 10 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 10;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti11():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 11 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 11;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti12():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 12 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 12;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti13():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 13 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 13;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti14():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 14 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 14;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti15():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 15 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 15;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti16():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 16 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 16;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti17():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 17 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 17;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti18():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 18 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 18;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti19():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 19 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 19;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti20():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 20 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 20;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti21():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 21 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 21;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti22():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 22 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 22;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti23():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 23 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 23;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti24():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 24 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 24;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()
    
def senti25():
    finalCount = 0
    
    #is the word 'good' present? == +1
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% good %');"
    cur.execute(sq)
    resulta = cur.fetchone()
    resultFinala = int(resulta[0])
    cur.close()
    conn.close()
    if resultFinala == 1:
        finalCount = finalCount + 1

    #is the word 'great' present? == +1
    conn2 = sqlite3.connect("test.db")
    cur2 = conn2.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% great %');"
    cur2.execute(sq)
    resultb = cur2.fetchone()
    resultFinalb = int(resultb[0])
    cur2.close()
    conn2.close()
    if resultFinalb == 1:
        finalCount = finalCount + 1

    #is the word 'happy' present? == +1
    conn3 = sqlite3.connect("test.db")
    cur3 = conn3.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% happy %');"
    cur3.execute(sq)
    resultc = cur3.fetchone()
    resultFinalc = int(resultc[0])
    cur3.close()
    conn3.close()
    if resultFinalc == 1:
        finalCount = finalCount + 1

    #is the word 'win' present? == +1
    conn4 = sqlite3.connect("test.db")
    cur4 = conn4.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% win %');"
    cur4.execute(sq)
    resultd = cur4.fetchone()
    resultFinald = int(resultd[0])
    cur4.close()
    conn4.close()
    if resultFinald == 1:
        finalCount = finalCount + 1

    #is the word 'love' present? == +1
    conn5 = sqlite3.connect("test.db")
    cur5 = conn5.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% love %');"
    cur5.execute(sq)
    resulte = cur5.fetchone()
    resultFinale = int(resulte[0])
    cur5.close()
    conn5.close()
    if resultFinale == 1:
        finalCount = finalCount + 1

    #is the word 'nice' present? == +1
    conn6 = sqlite3.connect("test.db")
    cur6 = conn6.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% nice %');"
    cur6.execute(sq)
    resultf = cur6.fetchone()
    resultFinalf = int(resultf[0])
    cur6.close()
    conn6.close()
    if resultFinalf == 1:
        finalCount = finalCount + 1

    #is the word 'authentic' present? == +1
    conn7 = sqlite3.connect("test.db")
    cur7 = conn7.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% authentic %');"
    cur7.execute(sq)
    resultg = cur7.fetchone()
    resultFinalg = int(resultg[0])
    cur7.close()
    conn7.close()
    if resultFinalg == 1:
        finalCount = finalCount + 1

    #is the word 'like' present? == +1
    conn8 = sqlite3.connect("test.db")
    cur8 = conn8.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% like %');"
    cur8.execute(sq)
    resulth = cur8.fetchone()
    resultFinalh = int(resulth[0])
    cur8.close()
    conn8.close()
    if resultFinalh == 1:
        finalCount = finalCount + 1

    #is the word 'fun' present? == +1
    conn9 = sqlite3.connect("test.db")
    cur9 = conn9.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% fun %');"
    cur9.execute(sq)
    resulti = cur9.fetchone()
    resultFinali = int(resulti[0])
    cur9.close()
    conn9.close()
    if resultFinali == 1:
        finalCount = finalCount + 1

    #is the word 'appreciate' present? == +1
    conn10 = sqlite3.connect("test.db")
    cur10 = conn10.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% appreciate %');"
    cur10.execute(sq)
    resultj = cur10.fetchone()
    resultFinalj = int(resultj[0])
    cur10.close()
    conn10.close()
    if resultFinalj == 1:
        finalCount = finalCount + 1

    #is the word 'fuck' present? == -1
    conn11 = sqlite3.connect("test.db")
    cur11 = conn11.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% good %');"
    cur11.execute(sq)
    resultk = cur11.fetchone()
    resultFinalk = int(resultk[0])
    cur11.close()
    conn11.close()
    if resultFinalk == 1:
        finalCount = finalCount - 1

    #is the word 'corrupt' present? == -1
    conn12 = sqlite3.connect("test.db")
    cur12 = conn12.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% corrupt %');"
    cur12.execute(sq)
    resultm = cur12.fetchone()
    resultFinalm = int(resultm[0])
    cur12.close()
    conn12.close()
    if resultFinalm == 1:
        finalCount = finalCount - 1

    #is the word 'stupid' present? == -1
    conn13 = sqlite3.connect("test.db")
    cur13 = conn13.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% stupid %');"
    cur13.execute(sq)
    resultn = cur13.fetchone()
    resultFinaln = int(resultn[0])
    cur13.close()
    conn13.close()
    if resultFinaln == 1:
        finalCount = finalCount - 1

    #is the word 'irrelevant' present? == -1
    conn14 = sqlite3.connect("test.db")
    cur14 = conn14.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% irrelevant %');"
    cur14.execute(sq)
    resulto = cur14.fetchone()
    resultFinalo = int(resulto[0])
    cur14.close()
    conn14.close()
    if resultFinalo == 1:
        finalCount = finalCount - 1

    #is the word 'colluding' present? == -1
    conn15 = sqlite3.connect("test.db")
    cur15 = conn15.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% colluding %');"
    cur15.execute(sq)
    resultp = cur15.fetchone()
    resultFinalp = int(resultp[0])
    cur15.close()
    conn15.close()
    if resultFinalp == 1:
        finalCount = finalCount - 1

    #is the word 'horrible' present? == -1
    conn16 = sqlite3.connect("test.db")
    cur16 = conn16.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% horrible %');"
    cur16.execute(sq)
    resultq = cur16.fetchone()
    resultFinalq = int(resultq[0])
    cur16.close()
    conn16.close()
    if resultFinalq == 1:
        finalCount = finalCount - 1

    #is the word 'unfair' present? == -1
    conn17 = sqlite3.connect("test.db")
    cur17 = conn17.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% unfair %');"
    cur17.execute(sq)
    resultr = cur17.fetchone()
    resultFinalr = int(resultr[0])
    cur17.close()
    conn17.close()
    if resultFinalr == 1:
        finalCount = finalCount - 1

    #is the word 'guilty' present? == -1
    conn18 = sqlite3.connect("test.db")
    cur18 = conn18.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% guilty %');"
    cur18.execute(sq)
    resultz = cur18.fetchone()
    resultFinalz = int(resultz[0])
    cur18.close()
    conn18.close()
    if resultFinalz == 1:
        finalCount = finalCount - 1

    #is the word 'foolish' present? == -1
    conn19 = sqlite3.connect("test.db")
    cur19 = conn19.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% foolish %');"
    cur19.execute(sq)
    resultx = cur19.fetchone()
    resultFinalx = int(resultx[0])
    cur19.close()
    conn19.close()
    if resultFinalx == 1:
        finalCount = finalCount - 1

    #is the word 'hateful' present? == -1
    conn20 = sqlite3.connect("test.db")
    cur20 = conn20.cursor()
    sq = "SELECT EXISTS (SELECT * FROM merge WHERE id = 25 AND comments LIKE '% hateful %');"
    cur20.execute(sq)
    resulty = cur20.fetchone()
    resultFinaly = int(resulty[0])
    cur20.close()
    conn20.close()
    if resultFinaly == 1:
        finalCount = finalCount - 1

    #adds final sentiment number to corresponding database row
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("UPDATE merge SET sent = ? WHERE id = 25;", [finalCount])
    conn.commit()
    cur.close()
    conn.close()

