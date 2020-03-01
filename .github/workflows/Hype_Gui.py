import tkinter as tk

main_application=tk.Tk()
main_application.iconbitmap('nasa_PLL_icon.ico')
main_application.title('Home     -     Hyperion Intelligent Lighting System')

main_canvas = tk.Canvas(main_application, height=1000, width=1000, bg='#9DD9F9')
main_canvas.grid()

crew_zones = 3
plant_zones = 1
all_zones = []

for i in range(0, crew_zones):
    all_zones.append('Crew Zone 'f'{i + 1}')
for i in range(0, plant_zones):
    all_zones.append('Plant Zone 'f'{i + 1}')

home_label = tk.Label(main_canvas, text='HOME', font=16, bg='#9DD9F9')
home_label.grid(row=0, column=0)

drop_select_zone=tk.StringVar()
drop_select_zone.set('SELECT YOUR ZONE')

def alerts():
    def home():
        main.destroy()

    """def all_alerts():
        all_alerts_window = tk.Toplevel(main)
        all_alerts_window.title('All Alerts     -     Hyperion Intelligent Lighting System')
        all_alerts_window.iconbitmap('nasa_PLL_icon.ico')

        all_alerts_canvas = tk.Canvas(all_alerts_window, height=100, width=100, bg='#9DD9F9')
        all_alerts_canvas.grid(row=0, column=0)
        all_alerts_label = tk.Label(all_alerts_canvas, text='A full list of alerts will be\ndisplayed in this window'
                                    , height=15, width=70, bg='#9DD9F9')
        all_alerts_label.grid(row=0, column=0)"""

    def all_logs():
        all_logs_window = tk.Toplevel(main)
        all_logs_window.title('All Logs     -     Hyperion Intelligent Lighting System')
        all_logs_window.iconbitmap('nasa_PLL_icon.ico')

        all_logs_canvas = tk.Canvas(all_logs_window, height=100, width=100, bg='#9DD9F9')
        all_logs_canvas.grid(row=0, column=0)
        all_logs_label = tk.Label(all_logs_canvas, text='A full list of logs will be\ndisplayed in this window'
                                  , height=15, width=70, bg='#9DD9F9')
        all_logs_label.grid(row=0, column=0)

    def alert_settings():
        alert_settings_window = tk.Toplevel(main)
        alert_settings_window.title('Alert Settings     -     Hyperion Intelligent Lighting System')
        alert_settings_window.iconbitmap('nasa_PLL_icon.ico')

        alert_settings_canvas = tk.Canvas(alert_settings_window, height=100, width=100, bg='#9DD9F9')
        alert_settings_canvas.grid(row=0, column=0)
        alert_settings_label = tk.Label(alert_settings_canvas, text='A list of actionable settings will'
                                                                    ' be\ndisplayed in this window', height=15,
                                        width=70, bg='#9DD9F9')
        alert_settings_label.grid(row=0, column=0)

    main = tk.Tk()
    main.title('Alerts     -     Hyperion Intelligent Lighting System')
    main.iconbitmap('nasa_PLL_icon.ico')
    color = '#F99D9D'
    warning_text = 'Placeholder for Warnings \n The text and color in this button will be dynamic\n ' \
                   'It will be based on the severity of most the recent warning'

    canvas = tk.Canvas(main, height=700, width=700, bg='#9DD9F9')
    canvas.grid()

    dummy_thicc_horiz = tk.Label(canvas, height=1, width=69, bg='#9DD9F9')
    dummy_thicc_horiz.grid(row=0, column=0)

    """warning_button = tk.Button(canvas, text=(warning_text), height=5, width=60, bg=(color), cursor='hand2')
    warning_button.grid(row=1, column=0)"""

    dummy_thicc_horiz = tk.Label(canvas, height=1, width=69, bg='#9DD9F9')
    dummy_thicc_horiz.grid(row=2, column=0)

    warnings_list_label = tk.Label(canvas, text='System Alerts Log', height=2, width=29, bg='#CCCACA', relief='solid')
    warnings_list_label.grid(row=3, column=0)

    list_frame = tk.Frame(canvas)
    list_frame.grid(row=4, column=0)

    list_scrollbar = tk.Scrollbar(list_frame)
    list_scrollbar.pack(side='right')

    warnings_list = tk.Listbox(list_frame, height=7, width=30, yscrollcommand=list_scrollbar.set)
    warnings_list.insert(1, 'This one is too hot!')
    warnings_list.insert(2, 'This one is too cold!')
    warnings_list.insert(3, 'This one is too tough!')
    warnings_list.insert(4, 'This one is too soft!')
    warnings_list.insert(5, 'This one is juuuust right')
    warnings_list.insert(6, 'Placeholder')
    warnings_list.insert(7, 'Placeholder')
    warnings_list.insert(8, 'Placeholder')
    warnings_list.insert(9, 'Placeholder')
    warnings_list.insert(10, 'Placeholder')
    warnings_list.pack(side='left')

    list_scrollbar.config(command=warnings_list.yview)

    dummy_thicc_horiz = tk.Label(canvas, height=1, width=69, bg='#9DD9F9')
    dummy_thicc_horiz.grid(row=5, column=0)

    settings_frame = tk.Frame(canvas, height=5, width=70, bg='#9DD9F9')
    settings_frame.grid(row=6, column=0)

    home_button = tk.Button(settings_frame, text='Home', height=3, width=15, bg='#3CA3DE', cursor='hand2',
                            command=(home))
    home_button.grid(row=0, column=0, padx=4)

    """all_alerts_button = tk.Button(settings_frame, text='All Alerts', height=3, width=15, bg='#3CA3DE', cursor='hand2',
                                  command=(all_alerts))
    all_alerts_button.grid(row=0, column=1, padx=4)"""

    all_logs_button = tk.Button(settings_frame, text='All Logs', height=3, width=15, bg='#3CA3DE', cursor='hand2',
                                command=(all_logs))
    all_logs_button.grid(row=0, column=2, padx=4)

    alert_settings_button = tk.Button(settings_frame, text='Alert Settings', height=3, width=15, bg='#3CA3DE',
                                      cursor='hand2',
                                      command=(alert_settings))
    alert_settings_button.grid(row=0, column=3, padx=4)


def modify_profiles_screen():
    modify_profiles_screen = tk.TopLevel()
    modify_profiles_screen.geometry('500x500')
    modify_profiles_screen.configure(background='#9DD9F9')
    modify_profiles_screen.iconbitmap('nasa_PLL_icon.ico')


# define settings screen from settings button
def settings_screen():
    settings_screen = tk.Toplevel()
    settings_screen.geometry('500x500')
    settings_screen.configure(background='#9DD9F9')
    settings_screen.iconbitmap('nasa_PLL_icon.ico')

    settings_screen = tk.Label(settings_screen, text='Settings', font=16, bg='#9DD9F9')
    settings_screen.grid(row=0, column=0)
    modify_profiles = tk.Button(settings_screen, text='Modify Profiles \n Add/Delete \n Adjust Cycles', padx=10, pady=15,
                             bg='#77dd77', activebackground='#90EE90')
    modify_profiles.grid(row=0, column=0)
    modify_system = tk.Button(settings_screen, text='Modify System \n [Initialization/Setup]',
                           bg='#77dd77', activebackground='#90EE90')
    modify_system.grid(row=0, column=0)

# define profile selection screen
def profile_screen(event):
    profile_screen = tk.Toplevel()
    profile_screen.geometry('500x500')
    profile_screen.configure(background='#9DD9F9')
    profile_screen.iconbitmap('nasa_PLL_icon.ico')

    # label for chosen zone from Home page OptionMenu
    zone_picked = tk.Label(profile_screen, text=(drop_select_zone.get()), font=16, bg='#9DD9F9')
    zone_picked.grid(row=0, column=0)
    ##put OptionsMenu with list of profiles (seperate crew and plant???)
    ##put enter_button2 for OptionMenu to new window (3rd window)

    ###space=Label(profile_screen,text=' ',bg='#9DD9F9')
    ###space.grid(row=2,column=0)
    # frame for alters/warnings for chosen zone
    frame_alerts2 = tk.LabelFrame(profile_screen, text=f'{drop_select_zone.get()} ALERTS/WARNINGS',
                               padx=88, pady=100, bg='#F99D9D')
    frame_alerts2.grid(row=0, column=0)
    alerts_appear2 = tk.Button(frame_alerts2, text='most recent alerts/warnings of zone', bg='#F99D9D', relief='sunken',
                               command=(alerts()))
    alerts_appear2.grid(row=0, column=0)
    user_settings = tk.Button(profile_screen, text='Settings', bg='#3CA3DE', activebackground='#9DD9F9',
                      command=settings_screen)
    user_settings.grid(row=0, column=0)
    # back to Home button
    home_button1 = tk.Button(profile_screen, text='Home', bg='#3CA3DE', activebackground='#9DD9F9')
    home_button1.grid(row=0, column=0)


# create drop-down containing list - list_zones
# Enter and Settings button
###space=Label(root,text=' ',bg='#9DD9F9')
###space.grid(row=2,column=0)
main_canvas.bind('<Return>', profile_screen)
drop_zones = tk.OptionMenu(main_canvas, drop_select_zone, *all_zones)
drop_zones.config(width=40, height=1, bg='#966fd6', activebackground='#b19cd9', font=1, anchor='w')
drop_zones.grid(row=2, column=8, columnspan=1, padx=5)
enter_button1 = tk.Button(main_canvas, text='Enter', command=(profile_screen), bg='#966fd6', activebackground='#b19cd9', pady=3,
                       padx=8)
enter_button1.bind('<Button-1>', profile_screen)
enter_button1.grid(row=2, column=9, columnspan=1)

# frame for alters/warnings for system
frame_alerts1 = tk.LabelFrame(main_canvas, text='SYSTEM ALERTS/WARNINGS', padx=120, pady=60, bg='#F99D9D')
frame_alerts1.grid(row=3, column=8, columnspan=2, pady=15)
alerts_appear1 = tk.Button(frame_alerts1, text='most recent system alerts/warnings', bg='#F99D9D', relief='sunken', command=(alerts))
alerts_appear1.grid(row=3, column=8)

# settings button
settings = tk.Button(main_canvas, text='Settings', bg='#3CA3DE', activebackground='#9DD9F9', command=(settings_screen))
settings.grid(row=0, column=0, padx=1)

# going back home destroys other windows




main_application.mainloop()
