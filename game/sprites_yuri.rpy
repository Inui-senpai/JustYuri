# This right here tells the code where the images and stuff are. If the pack's sprite files aren't in "mod_assets/yuri", then you can go ahead and change the directory below.
define ys_directory = "/yuri/" #Note: This *MUST* end with a "/"



# This is what generates the images. Don't mind it. Please don't touch it unless you know what you're doing.
init python:
    # Poses list.
    ys_poselist = {
        "1":[(0,0),"yuri/1l.png", (0,0),"yuri/1r.png", (0,0),"yuri/a.png"],
        "2":[(0,0),"yuri/1l.png", (0,0),"yuri/2r.png", (0,0),"yuri/a.png"],
        "3":[(0,0),"yuri/2l.png", (0,0),"yuri/2r.png", (0,0),"yuri/a.png"],
        "1b":[(0,0),"yuri/a.png", (0,0),"yuri/1bl.png", (0,0),"yuri/1br.png"],
        "2b":[(0,0),"yuri/a.png", (0,0),"yuri/1bl.png", (0,0),"yuri/2br.png"],
        "3b":[(0,0),"yuri/a.png", (0,0),"yuri/2bl.png", (0,0),"yuri/2br.png"],
        "2c":[(0,0),"yuri/1l.png", (0,0),ys_directory+"pose_cuts.png", (0,0),"yuri/a.png"],
        "3c":[(0,0),"yuri/2l.png", (0,0),ys_directory+"pose_cuts.png", (0,0),"yuri/a.png"]
    }
    # Details list.
    ys_detailslist = {
        "":[],
        "1a":[(480,265),ys_directory+"sweat.png"],
        "1b":[(387,238),ys_directory+"blush.png"],
        "1c":[], # + tears
        "2a":[(480,265),ys_directory+"sweat.png", (387,238),ys_directory+"blush.png"],
        "2b":[(387,238),ys_directory+"blush.png"], # + tears
        "2c":[(480,265),ys_directory+"sweat.png"], # + tears
        "3a":[(480,265),ys_directory+"sweat.png", (387,238),ys_directory+"blush.png"] # + tears
    }
    # Eyes list.
    ys_eyeslist = {
        "1a":[(360,196),ys_directory+"eyes1a.png"],
        "1b":[(360,196),ys_directory+"eyes1b.png"],
        "1c":[(360,196),ys_directory+"eyes1c.png"],
        "1d":[(360,196),ys_directory+"eyes1d.png"],
        "1e":[(360,196),ys_directory+"eyes1e.png"],
        "1f":[(360,196),ys_directory+"eyes1f.png"],
        "1g":[(360,196),ys_directory+"eyes1g.png"],
        "1h":[(360,196),ys_directory+"eyes1h.png"],
        "2a":[(360,196),ys_directory+"eyes2a.png"],
        "2b":[(360,196),ys_directory+"eyes2b.png"],
        "2c":[(360,196),ys_directory+"eyes2c.png"],
        "2d":[(360,196),ys_directory+"eyes2d.png"],
        "2e":[(360,196),ys_directory+"eyes2e.png"],
        "2f":[(360,196),ys_directory+"eyes2f.png"],
        "2g":[(360,196),ys_directory+"eyes2g.png"],
        "2h":[(360,196),ys_directory+"eyes2h.png"],
        "3a":[(360,196),ys_directory+"eyes3a.png"],
        "3b":[(360,196),ys_directory+"eyes3b.png"],
        "3c":[(360,196),ys_directory+"eyes3c.png"],
        "3d":[(360,196),ys_directory+"eyes3d.png"],
        "3e":[(360,196),ys_directory+"eyes3e.png"],
        "3f":[(360,196),ys_directory+"eyes3f.png"],
        "3g":[(360,196),ys_directory+"eyes3g.png"],
        "3h":[(360,196),ys_directory+"eyes3h.png"],
        "4a":[(360,196),ys_directory+"eyes4a.png"],
        "4b":[(360,196),ys_directory+"eyes4b.png"],
        "4c":[(360,196),ys_directory+"eyes4c.png"],
        "4d":[(360,196),ys_directory+"eyes4d.png"],
        "4e":[(360,196),ys_directory+"eyes4e.png"],
        "4f":[(360,196),ys_directory+"eyes4f.png"],
        "4g":[(360,196),ys_directory+"eyes4g.png"],
        "4h":[(360,196),ys_directory+"eyes4h.png"],
        "5a":[(360,196),ys_directory+"eyes5a.png"],
        "5b":[(360,196),ys_directory+"eyes5b.png"],
        "5c":[(360,196),ys_directory+"eyes5c.png"],
        "5d":[(360,196),ys_directory+"eyes5d.png"],
        "5e":[(360,196),ys_directory+"eyes5e.png"],
        "5f":[(360,196),ys_directory+"eyes5f.png"],
        "5g":[(360,196),ys_directory+"eyes5g.png"],
        "5h":[(360,196),ys_directory+"eyes5h.png"],
        "6a":[(360,196),ys_directory+"eyes6a.png"],
        "6b":[(360,196),ys_directory+"eyes6b.png"],
        "6c":[(360,196),ys_directory+"eyes6c.png"],
        "6d":[(360,196),ys_directory+"eyes6d.png"],
        "6e":[(360,196),ys_directory+"eyes6e.png"],
        "6f":[(360,196),ys_directory+"eyes6f.png"],
        "6g":[(360,196),ys_directory+"eyes6g.png"],
        "6h":[(360,196),ys_directory+"eyes6h.png"],
        "7a":[(360,196),ys_directory+"eyes7a.png"],
        "7b":[(360,196),ys_directory+"eyes7b.png"],
        "7c":[(360,196),ys_directory+"eyes7c.png"],
        "7d":[(360,196),ys_directory+"eyes7d.png"],
        "7e":[(360,196),ys_directory+"eyes7e.png"],
        "7f":[(360,196),ys_directory+"eyes7f.png"],
        "7g":[(360,196),ys_directory+"eyes7g.png"],
        "7h":[(360,196),ys_directory+"eyes7h.png"],
        "8a":[(360,196),ys_directory+"eyes8a.png"],
        "8b":[(360,196),ys_directory+"eyes8b.png"],
        "8c":[(360,196),ys_directory+"eyes8c.png"],
        "8d":[(360,196),ys_directory+"eyes8d.png"],
        "8e":[(360,196),ys_directory+"eyes8e.png"],
        "8f":[(360,196),ys_directory+"eyes8f.png"],
        "8g":[(360,196),ys_directory+"eyes8g.png"],
        "8h":[(360,196),ys_directory+"eyes8h.png"]
    }
    # Mouths list.
    ys_mouthlist = {
        "1":[(415,285),ys_directory+"mouth1.png"],
        "2":[(415,285),ys_directory+"mouth2.png"],
        "3":[(415,285),ys_directory+"mouth3.png"],
        "4":[(415,285),ys_directory+"mouth4.png"],
        "5":[(415,285),ys_directory+"mouth5.png"],
        "6":[(415,285),ys_directory+"mouth6.png"],
        "7":[(415,285),ys_directory+"mouth7.png"],
        "8":[(415,285),ys_directory+"mouth8.png"],
        "9":[(415,285),ys_directory+"mouth9.png"],
        "10":[(415,285),ys_directory+"mouth10.png"]
    }

    # The special poses.
    ys_poselist2 = {
        "4":[(0,0),"yuri/3.png", (0,0),"yuri/a2.png"],
        "4b":[(0,0),"yuri/a2.png", (0,0),"yuri/3b.png"]
    }
    # Details list for the special poses.
    ys_detailslist2 = {
        "":[],
        "1a":[(429,265),ys_directory+"2sweat1.png"],
        "1b":[(353,183),ys_directory+"2blush1.png"],
        "2a":[(429,265),ys_directory+"2sweat1.png", (353,183),ys_directory+"2blush1.png"]
    }
    # Eyes list for the special poses.
    ys_eyeslist2 = {
        "1a":[(359,205),ys_directory+"2eyes1a.png"],
        "1b":[(359,205),ys_directory+"2eyes1b.png"],
        "1c":[(359,205),ys_directory+"2eyes1c.png"],
        "2a":[(359,205),ys_directory+"2eyes2a.png"],
        "2b":[(359,205),ys_directory+"2eyes2b.png"],
        "2c":[(359,205),ys_directory+"2eyes2c.png"],
        "3a":[(359,205),ys_directory+"2eyes3a.png"],
        "3b":[(359,205),ys_directory+"2eyes3b.png"],
        "3c":[(359,205),ys_directory+"2eyes3c.png"],
        "4a":[(353,183),ys_directory+"2blush2.png"], # Completely blushed face.
    }
    # Mouths list for the special poses.
    ys_mouthlist2 = {
        "1":[(376,289),ys_directory+"2mouth1.png"],
        "2":[(376,289),ys_directory+"2mouth2.png"],
        "3":[(376,289),ys_directory+"2mouth3.png"],
        "4":[(376,289),ys_directory+"2mouth4.png"]
    }

    for ys_posename, ys_pose in ys_poselist.items():
        for ys_detailsname, ys_details in ys_detailslist.items():
            for ys_eyesname, ys_eyes in ys_eyeslist.items():
                for ys_mouthname, ys_mouth in ys_mouthlist.items():
                    renpy.image(
                        "yuri " + ys_posename+ys_eyesname+ys_mouthname+ys_detailsname,
                        im.Composite(
                            (960, 960),
                            *ys_pose+ys_eyes+ys_mouth+{
                                True:{
                                    "1":[(376,236),ys_directory+"tearsextra1.png"]+ys_details+[(374,239),ys_directory+"tears.png"],
                                    "2":[(371,236),ys_directory+"tearsextra2.png"]+ys_details+[(374,239),ys_directory+"tears.png"],
                                    "3":[(377,237),ys_directory+"tearsextra3.png"]+ys_details+[(374,239),ys_directory+"tears.png"],
                                    "4":ys_details+[(373,240),ys_directory+"tearsextra4.png"],
                                    "5":ys_details+[(372,238),ys_directory+"tearsextra5.png"],
                                    "6":[(377,234),ys_directory+"tearsextra6.png"]+ys_details+[(374,239),ys_directory+"tears.png"],
                                    "7":[(377,235),ys_directory+"tearsextra7.png"]+ys_details+[(374,239),ys_directory+"tears.png"],
                                    "8":ys_details+[(377,233),ys_directory+"tearsextra8.png"]
                                }.get(ys_eyesname[0],ys_details),
                                False:ys_details
                            }.get(ys_detailsname=="1c" or ys_detailsname=="2b" or ys_detailsname=="2c" or ys_detailsname=="3a", ys_details)
                        )
                    )

    for ys_posename2, ys_pose2 in ys_poselist2.items():
        for ys_detailsname2, ys_details2 in ys_detailslist2.items():
            for ys_eyesname2, ys_eyes2 in ys_eyeslist2.items():
                for ys_mouthname2, ys_mouth2 in ys_mouthlist2.items():
                    renpy.image(
                        "yuri " + ys_posename2+ys_eyesname2+ys_mouthname2+ys_detailsname2,
                        im.Composite(
                            (960, 960),
                            *ys_pose2+ys_eyes2+ys_mouth2+{
                                True:{
                                    "1a":[(431,267),ys_directory+"2sweat2.png"],
                                    "1b":[],
                                    "2a":[(431,267),ys_directory+"2sweat2.png"]
                                }.get(ys_detailsname2, ys_details2),
                                False:ys_details2
                            }.get(ys_eyesname2=="4a", ys_details2)
                        )
                    )

#valentines please kill me
image yuri 1da = "yuri/valentines/behind/yuri8v2.png"
image yuri 1db = "yuri/valentines/behind/yuri1v2.png"
image yuri 1dc = "yuri/valentines/behind/yuri5v2.png"
image yuri 1dd = "yuri/valentines/behind/yuri4v2.png"
init 20 python:
    renpy.image("yuri 1dg", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["3"]+ys_eyeslist["2d"]))
    renpy.image("yuri 1df", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["4"]+ys_eyeslist["6b"]))

    renpy.image("yuri 1di", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["1"]+ys_eyeslist["2d"]))
    renpy.image("yuri 1dj", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["2"]+ys_eyeslist["2d"]))
    renpy.image("yuri 1dk", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["4"]+ys_eyeslist["5b"]))
    renpy.image("yuri 1dm", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["1"]+ys_eyeslist["5c"]))

    renpy.image("yuri 1dn", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["7"]+ys_eyeslist["6e"]))
    renpy.image("yuri 1dq", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["2"]+ys_eyeslist["7e"]))
    renpy.image("yuri 1du", im.Composite((960, 960), (0,0), "yuri/valentines/behind/yuri1v2.png", *ys_mouthlist["1"]+ys_eyeslist["2f"]))
    renpy.image("yuri 2da", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["1"]+ys_eyeslist["1a"]))
    renpy.image("yuri 2df", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["4"]+ys_eyeslist["3b"]))
    renpy.image("yuri 2dj", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["2"]+ys_eyeslist["2d"]))
    renpy.image("yuri 2dl", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["4"]+ys_eyeslist["5c"]))

    renpy.image("yuri 3da", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["1"]+ys_eyeslist["1a"]))
    renpy.image("yuri 3db", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["2"]+ys_eyeslist["1b"]))
    renpy.image("yuri 3dc", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["1"]+ys_eyeslist["4b"]))
    renpy.image("yuri 3dd", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["2"]+ys_eyeslist["4b"]))
    renpy.image("yuri 3de", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["3"]+ys_eyeslist["3b"]))
    renpy.image("yuri 3dm", im.Composite((960, 960), (0,0), "yuri/valentines/up/yuri1v2.png", *ys_mouthlist["1"]+ys_eyeslist["5c"]))

