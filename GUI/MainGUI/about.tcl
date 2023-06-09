#############################################################################
# Generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#  Apr 20, 2023 11:57:52 AM CEST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m59" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 569x252+317+154
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1284 701
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    set toptitle "Toplevel 0"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    label "$top.lab47" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief groove -text "Label" 
    vTcl:DefineAlias "$top.lab47" "LogoContainer" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab47
    label "$top.lab48" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "AutoBulletin" 
    vTcl:DefineAlias "$top.lab48" "AppName" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab48
    label "$top.lab49" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "B.0.2" 
    vTcl:DefineAlias "$top.lab49" "AppVersion" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    vTcl:copy_lock $top.lab49
    label "$top.lab50" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "© LABARBE Léo, Mr Imloul" 
    vTcl:DefineAlias "$top.lab50" "AppCopyright" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$top.tSe51" \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe51" "VerticalSep" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    button "$top.but52" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Button" 
    vTcl:DefineAlias "$top.but52" "DonateButton" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    button "$top.but53" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Button" 
    vTcl:DefineAlias "$top.but53" "InstagramButton" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    button "$top.but54" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Button" 
    vTcl:DefineAlias "$top.but54" "SnapchatButton" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    button "$top.but55" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Button" 
    vTcl:DefineAlias "$top.but55" "GmailButton" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$top.tSe47"
    vTcl:DefineAlias "$top.tSe47" "HorizontalSep" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    label "$top.lab51" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "→ Curseurs :" 
    vTcl:DefineAlias "$top.lab51" "Cursors" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    label "$top.lab52" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9 -weight normal -slant roman -underline 1 -overstrike 0" \
        -foreground #5662eb -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "FlynMaker49" 
    vTcl:DefineAlias "$top.lab52" "CursorsUsername" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    label "$top.lab53" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "→ Sons :" 
    vTcl:DefineAlias "$top.lab53" "Sounds" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    label "$top.lab54" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9 -weight normal -slant roman -underline 1 -overstrike 0" \
        -foreground #5662eb -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Leszek Szary" 
    vTcl:DefineAlias "$top.lab54" "SoundsUsername1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    label "$top.lab55" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "," 
    vTcl:DefineAlias "$top.lab55" "Virgule" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    label "$top.lab56" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9 -weight normal -slant roman -underline 1 -overstrike 0" \
        -foreground #5662eb -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Kastenfrosch" 
    vTcl:DefineAlias "$top.lab56" "SoundsUsername2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    label "$top.lab57" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "→ Images Vectorielles :" 
    vTcl:DefineAlias "$top.lab57" "Image" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    label "$top.lab58" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 9 -weight normal -slant roman -underline 1 -overstrike 0" \
        -foreground #5662eb -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Flaticon" 
    vTcl:DefineAlias "$top.lab58" "ImageLink" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    menu "$top.m59" \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font "TkMenuFont" -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
### SPOT dump_widget_opt A
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab47 \
        -in $top -x 0 -relx 0.035 -y 0 -rely 0.087 -width 0 -relwidth 0.183 \
        -height 0 -relheight 0.413 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.253 -y 0 -rely 0.163 -width 0 -relwidth 0.288 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.251 -y 0 -rely 0.238 -width 0 -relwidth 0.253 \
        -height 0 -relheight 0.087 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 0 -relx 0.251 -y 0 -rely 0.333 -width 0 -relwidth 0.288 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.tSe51 \
        -in $top -x 0 -relx 0.545 -y 0 -rely 0.262 -width 0 -relwidth 0 \
        -height 0 -relheight 0.476 -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 0 -relx 0.629 -y 0 -rely 0.742 -width 162 -relwidth 0 \
        -height 35 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but53 \
        -in $top -x 0 -relx 0.629 -y 0 -rely 0.54 -width 162 -relwidth 0 \
        -height 35 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 0 -relx 0.629 -y 0 -rely 0.329 -width 162 -relwidth 0 \
        -height 35 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 0 -relx 0.629 -y 0 -rely 0.127 -width 162 -relwidth 0 \
        -height 35 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tSe47 \
        -in $top -x 0 -relx 0.097 -y 0 -rely 0.583 -width 0 -relwidth 0.35 \
        -height 0 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -relx 0.035 -y 0 -rely 0.635 -width 0 -relwidth 0.183 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.158 -y 0 -rely 0.635 -width 0 -relwidth 0.13 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 0 -relx 0.035 -y 0 -rely 0.734 -width 0 -relwidth 0.183 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -relx 0.125 -y 0 -rely 0.734 -width 0 -relwidth 0.13 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 0 -relx 0.243 -y 0 -rely 0.746 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 0 -relx 0.255 -y 0 -rely 0.734 -width 0 -relwidth 0.13 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 0 -relx 0.035 -y 0 -rely 0.833 -width 0 -relwidth 0.271 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.258 -y 0 -rely 0.833 -width 0 -relwidth 0.13 \
        -height 0 -relheight 0.083 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

