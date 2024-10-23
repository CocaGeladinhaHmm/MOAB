# -*- coding: utf-8 -*-
def t300706_1():
    """State 0"""
    while True:
        """State 13"""
        Label('L0')
        DebugEvent('最初')
        if CompareBonfireLevel(1, 0) == 1 and CompareBonfireState(1) == 1:
            break
        elif (CompareBonfireState(1) == 1 and HasDisableTalkPeriodElapsed() == 1 and not IsTalkingToSomeoneElse()
              and not CheckSelfDeath() and not IsCharacterDisabled() and not IsClientPlayer() and GetRelativeAngleBetweenPlayerAndSelf()
              <= 45 and GetDistanceToPlayer() <= 2 and CompareBonfireState(1) == 1 and CheckActionButtonArea(6100)):
            """State 12"""
            Label('L1')
            DebugEvent('人間性を捧げた')
            OfferHumanity()
            RequestUnlockTrophy(26)
            """State 11"""
            ClearTalkDisabledState()
            DebugEvent('会話タイマークリア　最初')
    while Loop('loop1'):
        """State 1"""
        Label('L2')
        DebugEvent('待機')
        SetUpdateDistance(10)
        if CompareBonfireLevel(0, 0) == 1:
            Goto('L0')
        elif CheckActionButtonArea(6101) and CompareBonfireState(1) == 1:
            """State 34"""
            StartBonfireAnimLoop()
            ClearTalkActionState()
            DisplayOneLineHelp(-1)
            ClearPlayerDamageInfo()
            SetEventState(760, 0)
            if CompareBonfireState(0) == 1:
                """State 9"""
                Label('L3')
                ForceEndTalk(0)
                ClearTalkProgressData()
                CloseShopMessage()
                DebugEvent('リスト強制開放')
                EndBonfireKindleAnimLoop()
            elif GetDistanceToPlayer() >= 8 or GetPlayerYDistance() > 1:
                Goto('L3')
            elif CompareBonfireState(1) == 1 and GetEventStatus(4084):
                while True:
                    """State 4"""
                    Label('L4')
                    ShowShopMessage(0, 0, 0)
                    DebugEvent('篝火リスト')
                    RequestSave(0)
                    AddTalkListData(1, 15000280, -1)
                    # action:15000005:"Leave"
                    AddTalkListData(98, 80000001, -1)
                    AddTalkListData(9, 15000005, -1)
                    def ExitPause():
                        ClearTalkListData()
                    if not GetTalkListEntryResult():
                        break
                    elif GetTalkListEntryResult() == 98:
                        assert t300706_x9999()
                    elif GetTalkListEntryResult() == 1:
                        """State 5"""
                        DebugEvent('逃げ帰る')
                        """State 6"""
                        # action:90000028:""
                        OpenGenericDialog(2, 90000028, 3, 4, 2)
                        if not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                            continue
                        elif GetGenericDialogButtonResult() == 2 and not IsGenericDialogOpen():
                            continue
                        elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                            """State 7"""
                            SetEventState(13000717, 1)
                            assert GetEventStatus(13000718) == 1
                            Goto('L3')
                    elif GetTalkListEntryResult() == 2:
                        """State 18"""
                        OpenEnhanceShop(0)
                        DebugEvent('武器強化')
                        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or
                              IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or
                              GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1):
                            pass
                        elif not IsMenuOpen(13):
                            continue
                    elif GetTalkListEntryResult() == 4:
                        """State 17"""
                        OpenRepairShop()
                        DebugEvent('修理ショップ')
                        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or
                              IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or
                              GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1):
                            pass
                        elif not IsMenuOpen(12):
                            continue
                    elif GetTalkListEntryResult() == 12:
                        """State 19"""
                        Label('L5')
                        StartWarpMenuInit()
                        DebugEvent('ワープメニューを開く')
                        if WasWarpMenuDestinationSelected() == 1:
                            """State 51"""
                            ForceEndTalk(0)
                            ClearTalkProgressData()
                            CloseShopMessage()
                            DebugEvent('リスト強制開放')
                            Goto('L18')
                        elif CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or
                              IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or
                              GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1):
                            pass
                        elif not IsMenuOpen(36):
                            continue
                    elif GetTalkListEntryResult() == 7 and GetEventStatus(706) == 1:
                        Goto('L5')
                    elif GetTalkListEntryResult() == 7 and not GetEventStatus(706):
                        """State 55"""
                        # action:10010712:"This bonfire is cut off from the others. Cannot warp."
                        OpenGenericDialog(7, 10010712, 1, 0, 2)
                        DebugEvent('ワープできない')
                        DisplayOneLineHelp(-1)
                        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                              == 1):
                            """State 47"""
                            Label('L6')
                            ForceCloseGenericDialog()
                            ForceEndTalk(0)
                            ClearTalkProgressData()
                            continue
                        elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or
                              IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or
                              GetDistanceToPlayer() > 8):
                            Goto('L6')
                        elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                            """State 48"""
                            Label('L7')
                            ClearTalkDisabledState()
                            DebugEvent('会話タイマークリア')
                            ClearTalkActionState()
                            ForceCloseGenericDialog()
                            continue
                        elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                            Goto('L7')
                    elif GetTalkListEntryResult() == 8:
                        """State 20"""
                        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif GetPlayerChrType() == 8:
                            """State 53"""
                            # action:10010725:"Cannot kindle while Hollowed"
                            OpenGenericDialog(7, 10010725, 1, 0, 2)
                            DebugEvent('亡者のときは注ぎ火できない')
                            DisplayOneLineHelp(-1)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                pass
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 8):
                                pass
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                """State 31"""
                                Label('L8')
                                ClearTalkDisabledState()
                                DebugEvent('会話タイマークリア')
                                ClearTalkActionState()
                                ForceCloseGenericDialog()
                                continue
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                Goto('L8')
                            """State 30"""
                            Label('L9')
                            ForceCloseGenericDialog()
                            ForceEndTalk(0)
                            ClearTalkProgressData()
                            continue
                        elif GetStatus(10) <= 1:
                            """State 28"""
                            # action:10010722:"No humanity"
                            OpenGenericDialog(7, 10010722, 1, 0, 2)
                            DebugEvent('人間性がない　リストから')
                            DisplayOneLineHelp(-1)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                Goto('L9')
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 8):
                                Goto('L9')
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                Goto('L8')
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                Goto('L8')
                        elif CompareBonfireLevel(0, 4) == 1:
                            """State 27"""
                            # action:10010723:"Cannot kindle any further"
                            OpenGenericDialog(7, 10010723, 1, 0, 2)
                            DebugEvent('これ以上捧げられない　解放後')
                            DisplayOneLineHelp(-1)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                """State 33"""
                                Label('L10')
                                ForceCloseGenericDialog()
                                ForceEndTalk(0)
                                ClearTalkProgressData()
                                continue
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 8):
                                Goto('L10')
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                """State 32"""
                                Label('L11')
                                ClearTalkDisabledState()
                                DebugEvent('会話タイマークリア')
                                ClearTalkActionState()
                                ForceCloseGenericDialog()
                                continue
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                Goto('L11')
                        elif CompareBonfireLevel(0, 2) == 1 and not GetEventStatus(257):
                            """State 52"""
                            # action:10010724:"Cannot kindle further without the secret rite"
                            OpenGenericDialog(7, 10010724, 1, 0, 2)
                            DebugEvent('これ以上捧げられない　解放前')
                            DisplayOneLineHelp(-1)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                Goto('L10')
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 8):
                                Goto('L10')
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                Goto('L11')
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                Goto('L11')
                        else:
                            """State 22"""
                            # action:10010741:"Offer humanity and kindle flame?"
                            OpenGenericDialog(8, 10010741, 3, 4, 2)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                """State 25"""
                                Label('L12')
                                ForceCloseGenericDialog()
                                ForceEndTalk(0)
                                ClearTalkProgressData()
                                continue
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 8):
                                Goto('L12')
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                pass
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                """State 24"""
                                DebugEvent('人間性を捧げた')
                                SetEventState(760, 1)
                                OfferHumanity()
                            elif GetGenericDialogButtonResult() == 2 and not IsGenericDialogOpen():
                                """State 23"""
                                DebugEvent('人間性を捧げない')
                            """State 26"""
                            ClearTalkDisabledState()
                            DebugEvent('会話タイマークリア　リストへ')
                            ClearTalkActionState()
                            ForceCloseGenericDialog()
                            if not GetEventStatus(760):
                                continue
                            elif (GetDistanceToPlayer() >= 8 or HasPlayerBeenAttacked() == 1 or (IsTalkingToSomeoneElse()
                                  or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
                                  1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                                  > 8)):
                                Continue('loop1')
                    elif GetTalkListEntryResult() == 10:
                        """State 38"""
                        DebugEvent('倉庫')
                        OpenRepository()
                        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or
                              IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or
                              GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1):
                            pass
                        elif not IsMenuOpen(26):
                            continue
                    elif GetTalkListEntryResult() == 5:
                        """State 21"""
                        OpenMagicEquip(10000, 10099)
                        DebugEvent('魔法装備ショップ')
                        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or
                              IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or
                              GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1):
                            pass
                        elif not IsMenuOpen(25):
                            continue
                    elif GetTalkListEntryResult() == 3:
                        """State 35"""
                        OpenEnhanceShop(10)
                        DebugEvent('防具強化')
                        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or
                              IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or
                              GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1):
                            pass
                        elif not IsMenuOpen(13):
                            continue
                    elif GetTalkListEntryResult() == 9:
                        break
                    elif GetTalkListEntryResult() == 11:
                        """State 39"""
                        DebugEvent('亡者から復活する')
                        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
                            pass
                        elif GetEventStatus(751) == 1:
                            """State 56"""
                            # action:10010736:"Cannot reverse Hollowing while cursed"
                            OpenGenericDialog(7, 10010736, 1, 0, 2)
                            DebugEvent('呪われている')
                            DisplayOneLineHelp(-1)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                Goto('L6')
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 8):
                                Goto('L6')
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                Goto('L7')
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                Goto('L7')
                        elif not GetPlayerChrType():
                            """State 45"""
                            # action:10010730:""
                            OpenGenericDialog(7, 10010730, 1, 0, 2)
                            DebugEvent('亡者ではない')
                            DisplayOneLineHelp(-1)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                """State 50"""
                                Label('L13')
                                ForceCloseGenericDialog()
                                ForceEndTalk(0)
                                ClearTalkProgressData()
                                continue
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 8):
                                Goto('L13')
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                """State 49"""
                                Label('L14')
                                ClearTalkDisabledState()
                                DebugEvent('会話タイマークリア')
                                ClearTalkActionState()
                                ForceCloseGenericDialog()
                                continue
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                Goto('L14')
                        elif GetStatus(10) <= 1:
                            """State 46"""
                            # action:10010731:"No humanity"
                            OpenGenericDialog(7, 10010731, 1, 0, 2)
                            DebugEvent('人間性がない')
                            DisplayOneLineHelp(-1)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                Goto('L6')
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf()
                                  > 120 or GetDistanceToPlayer() > 8):
                                Goto('L6')
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                Goto('L7')
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                Goto('L7')
                        else:
                            """State 40"""
                            # action:10010732:"Offer humanity and reverse Hollowing?"
                            OpenGenericDialog(8, 10010732, 3, 4, 2)
                            if (CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead()
                                == 1):
                                pass
                            elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                  or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                                  > 8):
                                pass
                            elif not GetGenericDialogButtonResult() and not IsGenericDialogOpen():
                                """State 41"""
                                Label('L15')
                                DebugEvent('人間性を捧げない')
                                """State 44"""
                                Label('L16')
                                ClearTalkDisabledState()
                                DebugEvent('会話タイマークリア　リストへ')
                                ClearTalkActionState()
                                ForceCloseGenericDialog()
                                if True:
                                    continue
                                elif (GetDistanceToPlayer() >= 8 or HasPlayerBeenAttacked() == 1 or (IsTalkingToSomeoneElse()
                                      or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer()
                                      == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                                      > 8)):
                                    Continue('loop1')
                            elif GetGenericDialogButtonResult() == 1 and not IsGenericDialogOpen():
                                """State 54"""
                                SetEventState(762, 1)
                                SetEventState(764, 1)
                                if IsPlayerDead() == 1:
                                    pass
                                elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                      or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                                      > 8):
                                    pass
                                elif not GetEventStatus(762):
                                    """State 42"""
                                    DebugEvent('人間性を捧げた')
                                    PlayerRespawn()
                                    ShowGrandioseTextPresentation(3)
                                    GiveSpEffectToPlayer(25)
                                    ChangePlayerStats(10, 1, 1)
                                    if IsPlayerDead() == 1:
                                        pass
                                    elif (GetDistanceToPlayer() >= 8 or HasPlayerBeenAttacked() == 1
                                          or (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled()
                                          or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer()
                                          > 8)):
                                        Continue('loop1')
                                    elif not IsMenuOpen(53) and not GetEventStatus(764):
                                        Goto('L16')
                            elif GetGenericDialogButtonResult() == 2 and not IsGenericDialogOpen():
                                Goto('L15')
                            """State 43"""
                            ForceCloseGenericDialog()
                            ForceEndTalk(0)
                            ClearTalkProgressData()
                            continue
                    """State 37"""
                    Label('L17')
                    CloseMenu()
                    DebugEvent('メッセージボックス閉じる')
                    EndBonfireKindleAnimLoop()
                    Goto('L3')
                """State 10"""
                EndBonfireKindleAnimLoop()
                Goto('L3')
            """State 29"""
            Label('L18')
            ClearTalkDisabledState()
            DebugEvent('会話タイマーをクリア　待機へ')
    """Unused"""
    """State 2"""
    # action:10010182:"Light bonfire"
    DisplayOneLineHelp(10010182)
    Goto('L2')
    """State 3"""
    DisplayOneLineHelp(-1)
    Goto('L2')
    """State 8"""
    OpenSoul()
    DebugEvent('ソウルショップ')
    if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
        Goto('L17')
    elif (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() ==
          1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance()
          > 1):
        Goto('L17')
    elif not IsMenuOpen(23):
        Goto('L4')
    """State 14"""
    DisplayOneLineHelp(-1)
    Goto('L1')
    """State 15"""
    DisplayOneLineHelp(-1)
    Goto('L0')
    """State 16"""
    # action:10010182:"Light bonfire"
    DisplayOneLineHelp(10010182)
    Goto('L0')
    """State 36"""
    DisplayOneLineHelp(-1)
    Goto('L2')

def t300706_x9002(action3=13010000):
    """State 0,1"""
    OpenGenericDialog(7, action3, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t300706_x9003(z1=150, goods1=2141, val1=14):
    """State 0,18"""
    # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10, goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
    call = t300706_x9005(goods2=150, goods3=0)
    if call.Get() == 1:
        """State 10,19"""
        # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10, goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
        call = t300706_x9005(goods2=150, goods3=1)
        if call.Get() == 1:
            """State 12,9"""
            if GetEstusAllocation(0) + GetEstusAllocation(1) < val1:
                """State 1"""
                # goods:2141:Estus Shard
                if ComparePlayerInventoryNumber(3, goods1, 2, 0, 0) == 1:
                    """State 2,14"""
                    # action:12002003:"Use <?gdsparam@2141?> to reinforce Estus Flask?"
                    call = t300706_x9006(action2=12002003)
                    if call.Get() == 0:
                        """State 4,6"""
                        # goods:2141:Estus Shard
                        PlayerEquipmentQuantityChange(3, goods1, -1)
                        """State 7"""
                        EstusAllocationUpdate(GetEstusAllocation(0) + 1, 0)
                        """State 16"""
                        # action:13002010:"Reinforced Estus Flask, increasing number of uses\n"
                        assert t300706_x9007(action1=13002010)
                        """State 22"""
                        assert t300706_x9008(val2=14)
                    elif call.Done():
                        """State 5"""
                        pass
                else:
                    """State 3,15"""
                    # action:13002011:"No <?gdsparam@2141?> in inventory"
                    assert t300706_x9007(action1=13002011)
            else:
                """State 8,17"""
                # action:13002012:"Cannot reinforce further"
                assert t300706_x9007(action1=13002012)
        elif call.Done():
            """State 13,21"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t300706_x9007(action1=13002014)
    elif call.Done():
        """State 11,20"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t300706_x9007(action1=13002013)
    """State 23"""
    return 0

def t300706_x9004(z2=150):
    """State 0,6"""
    # goods:151:Estus Flask, goods:153:Estus Flask+1, goods:155:Estus Flask+2, goods:157:Estus Flask+3, goods:159:Estus Flask+4, goods:161:Estus Flask+5, goods:163:Estus Flask+6, goods:165:Estus Flask+7, goods:167:Estus Flask+8, goods:169:Estus Flask+9, goods:171:Estus Flask+10, goods:150:Estus Flask, goods:152:Estus Flask+1, goods:154:Estus Flask+2, goods:156:Estus Flask+3, goods:158:Estus Flask+4, goods:160:Estus Flask+5, goods:162:Estus Flask+6, goods:164:Estus Flask+7, goods:166:Estus Flask+8, goods:168:Estus Flask+9, goods:170:Estus Flask+10
    call = t300706_x9005(goods2=150, goods3=0)
    if call.Get() == 1:
        """State 1,7"""
        # goods:191:Ashen Estus Flask, goods:193:Ashen Estus Flask+1, goods:195:Ashen Estus Flask+2, goods:197:Ashen Estus Flask+3, goods:199:Ashen Estus Flask+4, goods:201:Ashen Estus Flask+5, goods:203:Ashen Estus Flask+6, goods:205:Ashen Estus Flask+7, goods:207:Ashen Estus Flask+8, goods:209:Ashen Estus Flask+9, goods:211:Ashen Estus Flask+10, goods:190:Ashen Estus Flask, goods:192:Ashen Estus Flask+1, goods:194:Ashen Estus Flask+2, goods:196:Ashen Estus Flask+3, goods:198:Ashen Estus Flask+4, goods:200:Ashen Estus Flask+5, goods:202:Ashen Estus Flask+6, goods:204:Ashen Estus Flask+7, goods:206:Ashen Estus Flask+8, goods:208:Ashen Estus Flask+9, goods:210:Ashen Estus Flask+10
        call = t300706_x9005(goods2=150, goods3=1)
        if call.Get() == 1:
            """State 3,4"""
            OpenEstusAllotMenu()
            assert not (CheckSpecificPersonMenuIsOpen(14, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif call.Done():
            """State 5,9"""
            # action:13002014:"No <?gdsparam@190?> in inventory"
            assert t300706_x9007(action1=13002014)
    elif call.Done():
        """State 2,8"""
        # action:13002013:"No <?gdsparam@150?> in inventory"
        assert t300706_x9007(action1=13002013)
    """State 10"""
    return 0

def t300706_x9005(goods2=150, goods3=_):
    """State 0,1"""
    if (not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 0 * 2) and not IsEquipmentIDObtained(3,
        goods2 + 1 + goods3 * 40 + 1 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 +
        2 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 3 * 2) and not IsEquipmentIDObtained(3,
        goods2 + 1 + goods3 * 40 + 4 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 +
        5 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 6 * 2) and not IsEquipmentIDObtained(3,
        goods2 + 1 + goods3 * 40 + 7 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 +
        8 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 9 * 2)):
        """State 2"""
        if (not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 10 * 2) and not IsEquipmentIDObtained(3,
            goods2 + 1 + goods3 * 40 + 11 * 2) and not IsEquipmentIDObtained(3, goods2 + 12 + goods3
            * 40 + 12 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 13 * 2) and not
            IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 14 * 2) and not IsEquipmentIDObtained(3,
            goods2 + 1 + goods3 * 40 + 15 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 *
            40 + 16 * 2) and not IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 17 * 2) and not
            IsEquipmentIDObtained(3, goods2 + 1 + goods3 * 40 + 18 * 2) and not IsEquipmentIDObtained(3,
            goods2 + 1 + goods3 * 40 + 19 * 2)):
            """State 3"""
            if (not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 0 * 2) and not IsEquipmentIDObtained(3,
                goods2 + 0 + goods3 * 40 + 1 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3
                * 40 + 2 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 3 * 2) and
                not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 4 * 2) and not IsEquipmentIDObtained(3,
                goods2 + 0 + goods3 * 40 + 5 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3
                * 40 + 6 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 7 * 2) and
                not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 8 * 2) and not IsEquipmentIDObtained(3,
                goods2 + 0 + goods3 * 40 + 9 * 2)):
                """State 4"""
                if (not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 10 * 2) and not IsEquipmentIDObtained(3,
                    goods2 + 0 + goods3 * 40 + 11 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 +
                    goods3 * 40 + 12 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 +
                    13 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 14 * 2) and not
                    IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 15 * 2) and not IsEquipmentIDObtained(3,
                    goods2 + 0 + goods3 * 40 + 16 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 +
                    goods3 * 40 + 17 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 +
                    18 * 2) and not IsEquipmentIDObtained(3, goods2 + 0 + goods3 * 40 + 19 * 2)):
                    """State 5"""
                    return 0
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
    """State 6"""
    return 1

def t300706_x9006(action2=12002003):
    """State 0,1"""
    # action:12002003:"Use <?gdsparam@2141?> to reinforce Estus Flask?"
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t300706_x9007(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t300706_x9008(val2=14):
    """State 0,3"""
    if GetEstusAllocation(0) + GetEstusAllocation(1) < val2:
        """State 2"""
        pass
    else:
        """State 1,4"""
        RequestUnlockTrophy(16)
    """State 5"""
    return 0

def t300706_x9999():
    """State 0"""
    assert GetCurrentStateElapsedTime() > 0.1
    while True:
        """State 1"""
        MainBonfireMenuFlag()
        ClearTalkListData()
        # action:15002000:"Level Up"
        AddTalkListData(1, 15002000, -1)
        # action:15011020:"Purchase Item"
        AddTalkListData(2, 15011020, -1)
        # action:15000012:"Sell Item"
        AddTalkListData(3, 15000012, -1)
        # action:15010002:"Reinforce Weapon"
        AddTalkListData(4, 15010002, -1)
        # action:15010001:"Infuse Weapon"
        AddTalkListData(5, 15010001, -1)
        # action:15010003:"Repair Equipment"
        AddTalkListData(6, 15010003, -1)
        # action:15002002:"Allot Estus"
        AddTalkListData(7, 15002002, -1)
        # action:15002003:"Reinforce Estus Flask"
        AddTalkListData(8, 15002003, -1)
        AddTalkListData(9, 15027010, -1)
        AddTalkListData(10, 15027011, -1)
        # action:15000005:"Leave"
        AddTalkListData(99, 15000005, -1)
        ShowShopMessage(1)
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenSoul()
            assert not (CheckSpecificPersonMenuIsOpen(10, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            OpenRegularShop(110000, 119899)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 4:
            """State 7"""
            if GetEventStatus(2051) == 1 or IsMultiplayerInProgress() == 1:
                """State 21,27"""
                assert t300706_x9002(action3=13010000)
            else:
                """State 17"""
                CombineMenuFlagAndEventFlag(6001, 232)
                CombineMenuFlagAndEventFlag(6001, 233)
                CombineMenuFlagAndEventFlag(6001, 234)
                """State 9"""
                OpenEnhanceShop(0)
                assert not (CheckSpecificPersonMenuIsOpen(9, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 5:
            """State 8"""
            CombineMenuFlagAndEventFlag(6001, 344)
            CombineMenuFlagAndEventFlag(6001, 337)
            CombineMenuFlagAndEventFlag(6001, 334)
            CombineMenuFlagAndEventFlag(300, 332)
            CombineMenuFlagAndEventFlag(300, 333)
            CombineMenuFlagAndEventFlag(300, 342)
            CombineMenuFlagAndEventFlag(301, 335)
            CombineMenuFlagAndEventFlag(301, 345)
            CombineMenuFlagAndEventFlag(301, 340)
            CombineMenuFlagAndEventFlag(302, 336)
            CombineMenuFlagAndEventFlag(302, 338)
            CombineMenuFlagAndEventFlag(302, 339)
            CombineMenuFlagAndEventFlag(303, 341)
            CombineMenuFlagAndEventFlag(303, 343)
            CombineMenuFlagAndEventFlag(303, 346)
            CombineMenuFlagAndEventFlag(6000, 347)
            CombineMenuFlagAndEventFlag(6001, 331)
            """State 6"""
            OpenEquipmentChangeOfPurposeShop()
            assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 6:
            """State 10"""
            OpenRepairShop()
            assert not (CheckSpecificPersonMenuIsOpen(8, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 7:
            """State 20,26"""
            assert t300706_x9004(z2=150) and not (CheckSpecificPersonMenuIsOpen(8, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 8:
            """State 19,25"""
            # goods:2141:Estus Shard
            assert (t300706_x9003(z1=150, goods1=2141, val1=14) and not (CheckSpecificPersonMenuIsOpen(8,
                    0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)))
        elif GetTalkListEntryResult() == 9:
            ReallocateAttributes()
            ClearTalkActionState()
            def ExitPause():
                SetEventState(73500161, 0)
            assert not (CheckSpecificPersonMenuIsOpen(19, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 10:
            OpenCharaMakeMenu()
            ClearTalkActionState()
            def ExitPause():
                SetEventState(73500161, 0)
            assert not (CheckSpecificPersonMenuIsOpen(16, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif (GetTalkListEntryResult() == 99 or not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not
              CheckSpecificPersonGenericDialogIsOpen(0))):
            """State 5,22"""
            return 0