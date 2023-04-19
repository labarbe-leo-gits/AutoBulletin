#############################################################################
# Generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#  Mar 07, 2023 03:37:44 PM CET  platform: Windows NT
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
        -menu "$top.m52" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 452x457+393+76
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
    set toptitle "AutoBulletin - B.0.2"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl::widgets::core::popup::createCmd "$top.pop47" \
        -activebackground $vTcl(analog_color_m) -activeborderwidth 1 \
        -activeforeground black -background $vTcl(actual_gui_bg) \
        -borderwidth 1 -disabledforeground #a3a3a3 -font "TkMenuFont" \
        -foreground $vTcl(actual_gui_fg) -tearoff 1 
    global vTcl
    set val vTcl($top.pop47,-proc)
    set vTcl($top.pop47,-proc) popup1
    namespace eval ::widgets::$top.pop47 {}
    set ::widgets::$top.pop47::ClassOption(-proc) popup1
    set ::widgets::$top.pop47::options(-proc) popup1
    set ::widgets::$top.pop47::save(-proc) 1
    vTcl:DefineAlias "$top.pop47" "Popupmenu1" vTcl:WidgetProc "" 1
### SPOT dump_widget_opt A
    entry "$top.ent48" \
        -background white -disabledforeground #a3a3a3 -font "TkFixedFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 264 
    vTcl:DefineAlias "$top.ent48" "DropownPlaceHolder" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$top.tSe49"
    vTcl:DefineAlias "$top.tSe49" "TSeparator1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    menu "$top.m52" \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font "TkMenuFont" -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
### SPOT dump_widget_opt A
    button "$top.but53" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Générer l'appréciation" 
    vTcl:DefineAlias "$top.but53" "Gen" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    button "$top.but54" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Générer & écrire l'appréciation" 
    vTcl:DefineAlias "$top.but54" "Gen_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$top.tSe47"
    vTcl:DefineAlias "$top.tSe47" "TSeparator1_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    frame "$top.fra54" \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 155 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 135 
    vTcl:DefineAlias "$top.fra54" "Frame1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.fra54
    label "$site_3_0.lab55" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Bavardages" 
    vTcl:DefineAlias "$site_3_0.lab55" "Label3" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad56" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Modérés" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad56" "Radiobutton1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad58" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Inexistants" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad58" "Radiobutton1_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad61" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Très Présents" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad61" "Radiobutton1_2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$site_3_0.tSe62"
    vTcl:DefineAlias "$site_3_0.tSe62" "TSeparator3" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.111 -y 0 -rely 0.019 -width 0 \
        -relwidth 0.77 -height 0 -relheight 0.284 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad56 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.439 -width 0 \
        -relwidth 0.504 -height 0 -relheight 0.335 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad58 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.639 -width 0 \
        -relwidth 0.652 -height 0 -relheight 0.348 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad61 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.271 -width 0 \
        -relwidth 0.726 -height 0 -relheight 0.271 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe62 \
        -in $site_3_0 -x 0 -relx 0.237 -y 0 -rely 0.271 -width 0 \
        -relwidth 0.519 -height 0 -relheight 0 -anchor nw -bordermode ignore 
    entry "$top.ent47" \
        -background white -disabledforeground #a3a3a3 -font "TkFixedFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 264 
    vTcl:DefineAlias "$top.ent47" "DropownPlaceHolder_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    frame "$top.fra49" \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 155 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 135 
    vTcl:DefineAlias "$top.fra49" "Frame1_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.fra49
    label "$site_3_0.lab55" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Sérieux" 
    vTcl:DefineAlias "$site_3_0.lab55" "Label3_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad56" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Dissipé (Rarement)" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad56" "Radiobutton1_3" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad58" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Souvent Ailleurs" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad58" "Radiobutton1_1_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad61" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Sérieux" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad61" "Radiobutton1_2_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$site_3_0.tSe62"
    vTcl:DefineAlias "$site_3_0.tSe62" "TSeparator3_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.111 -y 0 -rely 0.019 -width 0 \
        -relwidth 0.77 -height 0 -relheight 0.284 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad56 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.335 -width 0 \
        -relwidth 0.874 -height 0 -relheight 0.529 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad58 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.639 -width 0 \
        -relwidth 0.874 -height 0 -relheight 0.348 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad61 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.271 -width 0 \
        -relwidth 0.726 -height 0 -relheight 0.271 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe62 \
        -in $site_3_0 -x 0 -relx 0.215 -y 0 -rely 0.271 -width 0 \
        -relwidth 0.519 -height 0 -relheight 0 -anchor nw -bordermode ignore 
    frame "$top.fra47" \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 155 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 135 
    vTcl:DefineAlias "$top.fra47" "Frame1_2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.fra47
    label "$site_3_0.lab55" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Assiduitée" 
    vTcl:DefineAlias "$site_3_0.lab55" "Label3_2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad56" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Quelques Oublis" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad56" "Radiobutton1_4" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad58" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Non-Assidu" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad58" "Radiobutton1_1_2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad61" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Assidu" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad61" "Radiobutton1_2_2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$site_3_0.tSe62"
    vTcl:DefineAlias "$site_3_0.tSe62" "TSeparator3_2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.111 -y 0 -rely 0.019 -width 0 \
        -relwidth 0.77 -height 0 -relheight 0.284 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad56 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.439 -width 0 \
        -relwidth 0.874 -height 0 -relheight 0.335 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad58 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.639 -width 0 \
        -relwidth 0.874 -height 0 -relheight 0.348 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad61 \
        -in $site_3_0 -x 0 -relx 0.074 -y 0 -rely 0.271 -width 0 \
        -relwidth 0.726 -height 0 -relheight 0.271 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe62 \
        -in $site_3_0 -x 0 -relx 0.237 -y 0 -rely 0.271 -width 0 \
        -relwidth 0.519 -height 0 -relheight 0 -anchor nw -bordermode ignore 
    frame "$top.fra48" \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 93 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 205 
    vTcl:DefineAlias "$top.fra48" "Frame2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.fra48
    label "$site_3_0.lab51" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Participation" 
    vTcl:DefineAlias "$site_3_0.lab51" "Label1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$site_3_0.tSe53"
    vTcl:DefineAlias "$site_3_0.tSe53" "TSeparator3_2_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad54" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Régulière" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad54" "Radiobutton1_2_3" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad48" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Hésitante" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad48" "Radiobutton1_2_3_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad49" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Inexistante" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad49" "Radiobutton1_2_3_2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$site_3_0.tSe50" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe50" "TSeparator2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.19 -y 0 -rely 0.108 -width 0 \
        -relwidth 0.588 -height 0 -relheight 0.226 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe53 \
        -in $site_3_0 -x 0 -relx 0.318 -y 0 -rely 0.387 -width 0 \
        -relwidth 0.332 -height 0 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.rad54 \
        -in $site_3_0 -x 0 -relx 0.081 -y 0 -rely 0.409 -width 0 \
        -relwidth 0.37 -height 0 -relheight 0.344 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad48 \
        -in $site_3_0 -x 0 -relx 0.081 -y 0 -rely 0.688 -width 0 \
        -relwidth 0.37 -height 0 -relheight 0.237 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad49 \
        -in $site_3_0 -x 0 -relx 0.521 -y 0 -rely 0.57 -width 0 \
        -relwidth 0.417 -height 0 -relheight 0.237 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe50 \
        -in $site_3_0 -x 0 -relx 0.474 -y 0 -rely 0.516 -width 0 -relwidth 0 \
        -height 0 -relheight 0.323 -anchor nw -bordermode ignore 
    frame "$top.fra51" \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 93 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 205 
    vTcl:DefineAlias "$top.fra51" "Frame2_2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.fra51
    label "$site_3_0.lab51" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Yu Gothic UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Résultats" 
    vTcl:DefineAlias "$site_3_0.lab51" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$site_3_0.tSe53"
    vTcl:DefineAlias "$site_3_0.tSe53" "TSeparator3_2_1_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad54" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Excellents" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad54" "Radiobutton1_2_3_3" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad48" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Bon" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad48" "Radiobutton1_2_3_1_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad49" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Efforts" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad49" "Radiobutton1_2_3_2_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::separator "$site_3_0.tSe50" \
        -orient vertical 
    vTcl:DefineAlias "$site_3_0.tSe50" "TSeparator2_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    radiobutton "$site_3_0.rad53" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 8 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -selectcolor #d9d9d9 -text "Insuffisants" \
        -variable "selectedButton" 
    vTcl:DefineAlias "$site_3_0.rad53" "Radiobutton1_2_3_2_1_1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.19 -y 0 -rely 0.108 -width 0 \
        -relwidth 0.588 -height 0 -relheight 0.226 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe53 \
        -in $site_3_0 -x 0 -relx 0.318 -y 0 -rely 0.387 -width 0 \
        -relwidth 0.332 -height 0 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.rad54 \
        -in $site_3_0 -x 0 -relx 0.081 -y 0 -rely 0.409 -width 0 \
        -relwidth 0.37 -height 0 -relheight 0.344 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad48 \
        -in $site_3_0 -x 0 -relx 0.081 -y 0 -rely 0.688 -width 0 \
        -relwidth 0.37 -height 0 -relheight 0.237 -anchor nw \
        -bordermode ignore 
    place $site_3_0.rad49 \
        -in $site_3_0 -x 0 -relx 0.521 -y 0 -rely 0.473 -width 0 \
        -relwidth 0.417 -height 0 -relheight 0.237 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tSe50 \
        -in $site_3_0 -x 0 -relx 0.474 -y 0 -rely 0.516 -width 0 -relwidth 0 \
        -height 0 -relheight 0.323 -anchor nw -bordermode ignore 
    place $site_3_0.rad53 \
        -in $site_3_0 -x 0 -relx 0.521 -y 0 -rely 0.699 -width 0 \
        -relwidth 0.417 -height 0 -relheight 0.237 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent48 \
        -in $top -x 0 -relx 0.199 -y 0 -rely 0.031 -width 264 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tSe49 \
        -in $top -x 0 -relx 0.268 -y 0 -rely 0.164 -width 0 -relwidth 0.442 \
        -height 0 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but53 \
        -in $top -x 0 -relx -0.027 -y 0 -rely 0.807 -width 477 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 0 -relx -0.027 -y 0 -rely 0.899 -width 477 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tSe47 \
        -in $top -x 0 -relx 0.277 -y 0 -rely 0.777 -width 0 -relwidth 0.442 \
        -height 0 -relheight 0 -anchor nw -bordermode ignore 
    place $top.fra54 \
        -in $top -x 0 -relx 0.022 -y 0 -rely 0.197 -width 0 -relwidth 0.299 \
        -height 0 -relheight 0.339 -anchor nw -bordermode ignore 
    place $top.ent47 \
        -in $top -x 0 -relx 0.199 -y 0 -rely 0.092 -width 264 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.fra49 \
        -in $top -x 0 -relx 0.679 -y 0 -rely 0.197 -width 0 -relwidth 0.299 \
        -height 0 -relheight 0.339 -anchor nw -bordermode ignore 
    place $top.fra47 \
        -in $top -x 0 -relx 0.352 -y 0 -rely 0.197 -width 0 -relwidth 0.299 \
        -height 0 -relheight 0.339 -anchor nw -bordermode ignore 
    place $top.fra48 \
        -in $top -x 0 -relx 0.022 -y 0 -rely 0.547 -width 0 -relwidth 0.467 \
        -height 0 -relheight 0.204 -anchor nw -bordermode ignore 
    place $top.fra51 \
        -in $top -x 0 -relx 0.511 -y 0 -rely 0.547 -width 0 -relwidth 0.467 \
        -height 0 -relheight 0.204 -anchor nw -bordermode ignore 

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
