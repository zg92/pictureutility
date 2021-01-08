import tkinter as tk, os, shutil, json
from PIL import Image

class pug_main:
    def __init__(self, master, user_info):
        self.master = master
        self.user_info = user_info
        self.destination_drive = user_info['destination_drive']
        self.source_drive = user_info['source_drive']
        self.final_source = user_info['final_source']
        self.final_dest = user_info['final_dest']
        self.instagramify_root = user_info['instagramify_root']
        self.dir_name = ''
        self.final_picture_list = []
        self.master.title('PUG V1')
        self.master.configure(bg='grey')

        self.top_frame = tk.Frame(self.master, bg='grey')
        self.top_frame.grid(row=0,column=0, padx=4)
        self.widget_title = tk.Label(self.top_frame, text='Picture Utility GUI', bg='grey')
        self.widget_title.grid(row=0, column=0)

        self.console = tk.Text(self.top_frame, height=1, width=121,fg='blue')
        self.console.grid(row=2, column=0, pady=4)
        self.console.insert('1.0', 'Welcome to the PUG! Fill out the boxes below to get started!')

        self.source_box_frame = tk.Frame(self.master, bg='grey')
        self.source_box_frame.grid(row=1, column=0, padx=4)

        self.enter_source_path = tk.Text(self.source_box_frame, height=1, borderwidth=2)
        self.enter_source_path.grid(column=0, row=0,pady=2)
        self.enter_source_path.insert('1.0', self.source_drive)
        self.save_source_var = tk.BooleanVar(self.source_box_frame)
        self.save_source_box = tk.Checkbutton(self.source_box_frame, var=self.save_source_var, text='Save Entry', bg='grey')
        self.save_source_box.grid(column=1, row=0)
        self.submit_source_path = tk.Button(self.source_box_frame, text='Submit Source', command=self.send_file_source, borderwidth=2, relief="raised",width=20)
        self.submit_source_path.grid(column=2, row=0)

        self.enter_destination_path = tk.Text(self.source_box_frame, height=1,borderwidth=2)
        self.enter_destination_path.grid(column=0,row=1,pady=2)
        self.enter_destination_path.insert('1.0', self.destination_drive)
        self.save_destination_var = tk.BooleanVar(self.source_box_frame)
        self.save_destination_box = tk.Checkbutton(self.source_box_frame, var=self.save_destination_var, text='Save Entry', bg='grey')
        self.save_destination_box.grid(column=1,row=1)
        self.submit_destination_path = tk.Button(self.source_box_frame, text='Submit Destination', command=self.send_file_destination, borderwidth=2, relief="raised",width=20)
        self.submit_destination_path.grid(column=2,row=1)

        self.enter_final_file_path = tk.Text(self.source_box_frame, height=1,borderwidth=2)
        self.enter_final_file_path.grid(column=0,row=2,pady=2)
        self.enter_final_file_path.insert('1.0', self.final_source)
        self.save_final_file_var = tk.BooleanVar(self.source_box_frame)
        self.save_final_file_box = tk.Checkbutton(self.source_box_frame, var=self.save_final_file_var, text='Save Entry', bg='grey')
        self.save_final_file_box.grid(column=1,row=2)
        self.submit_final_file_path = tk.Button(self.source_box_frame, text='Submit Final Source', borderwidth=2, relief="raised",width=20, command=self.final_files_source)
        self.submit_final_file_path.grid(column=2,row=2)

        self.enter_final_destination_path = tk.Text(self.source_box_frame, height=1,borderwidth=2)
        self.enter_final_destination_path.grid(column=0,row=3,pady=2)
        self.enter_final_destination_path.insert('1.0', self.final_dest)
        self.save_final_destination_var = tk.BooleanVar(self.source_box_frame)
        self.save_final_destination_box = tk.Checkbutton(self.source_box_frame, var=self.save_final_destination_var, text='Save Entry', bg='grey')
        self.save_final_destination_box.grid(column=1,row=3)
        self.submit_final_destination_path = tk.Button(self.source_box_frame, text='Submit Final Destination', borderwidth=2, relief="raised",width=20, command=self.final_files_destination)
        self.submit_final_destination_path.grid(column=2,row=3)
        
        self.textbox_frame2 = tk.Frame(self.master, bg='grey')
        self.textbox_frame2.grid(row=2, column=0, pady=4, padx=4)
        self.final_files = tk.Text(self.textbox_frame2, borderwidth=2, width=59,pady=2)
        self.final_files.grid(column=0, row=0, padx=2,pady=2)
        self.populate_files = tk.Button(self.textbox_frame2, text='Populate Files',borderwidth=2, relief="groove",width=47, command=self.populate_final_files)
        self.populate_files.grid(column=0,row=1,padx=2)
        self.move_files_populated = tk.Button(self.textbox_frame2, text='Move Populated',borderwidth=2, relief="groove",width=47, command=self.move_populated_final_files)
        self.move_files_populated.grid(column=0,row=2,padx=2)
        self.files_to_move = tk.Text(self.textbox_frame2, borderwidth=2,width=59)
        self.files_to_move.grid(column=1, row=0,pady=2,padx=2)
        self.show_files = tk.Button(self.textbox_frame2, text='Show Files', command=self.show_files, borderwidth=2, relief="groove", width=47)
        self.show_files.grid(column=1, row=1,pady=2,padx=2)
        self.move_files = tk.Button(self.textbox_frame2, text='Move Files', command=self.move_files, borderwidth=2, relief="groove",width=47)
        self.move_files.grid(column=1, row=2)

        self.textbox_frame3 = tk.Frame(self.master,bg='grey')
        self.textbox_frame3.grid(row=3, column=0, padx=4,pady=2)
        self.dest_dir_name = tk.Text(self.textbox_frame3, height=1,borderwidth=2,width=81)
        self.dest_dir_name.grid(column=0,row=0,padx=4,pady=2)
        self.dest_dir_name_submit = tk.Button(self.textbox_frame3, text='Enter Dir Name', borderwidth=2, relief="groove",width=29,padx=4, command= self.dir_name_submit)
        self.dest_dir_name_submit.grid(column=2,row=0,padx=4)
        self.ig_photo_root = tk.Text(self.textbox_frame3, height=1,borderwidth=2,width=81)
        self.ig_photo_root.grid(column=0,row=1,padx=4)
        self.instabutton_root = tk.Button(self.textbox_frame3, text='Enter Instagramify Root', borderwidth=2, relief="groove",width=29,padx=4, command=self.enter_instagramify_root)
        self.instabutton_root.grid(column=2,row=1,padx=4)
        self.ig_photo_root.insert('1.0', self.instagramify_root)
        self.ig_photo_name = tk.Text(self.textbox_frame3, height=1,borderwidth=2,width=81)
        self.ig_photo_name.grid(column=0,row=2,padx=4,pady=2)
        self.instabutton = tk.Button(self.textbox_frame3, text='Instagramify Photo', command=self.ig_ify, borderwidth=2, relief="groove",width=29,padx=4)
        self.instabutton.grid(column=2,row=2,pady=2,padx=4)


    def send_file_source(self): 
        self.source_drive = self.enter_source_path.get("1.0", "end-1c")
        self.user_info['source_drive'] = self.source_drive
        if self.save_source_var.get() == True:
            with open('pug_userinfo.txt','w') as fp:
                json.dump(self.user_info,fp)
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'File Source Has Been Saved and Submitted!')
            self.enter_source_path.configure(bg='#d4d4d4')
        else:
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'File Source Has Been Submitted!')


    def send_file_destination(self):
        self.destination_drive = self.enter_destination_path.get("1.0", "end-1c")
        self.user_info['destination_drive'] = self.destination_drive
        if self.save_destination_var.get() == True:
            with open('pug_userinfo.txt','w') as fp:
                json.dump(self.user_info, fp)
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'File Destination Has Been Saved and Submitted!')
            self.enter_destination_path.configure(bg='#d4d4d4')
        else:
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'File Destination Has Been Submitted!')

    def final_files_source(self):
        self.final_source = self.enter_final_file_path.get("1.0", "end-1c")
        self.user_info['final_source'] = self.final_source.rstrip('/')
        if self.save_final_file_var.get() == True:
            with open('pug_userinfo.txt','w') as fp:
                json.dump(self.user_info, fp)
                self.enter_final_file_path.configure(bg='#d4d4d4')
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Final Source Has Been Saved and Submitted!')
        else:
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Final Source Has Been Submitted!')

    def final_files_destination(self):
        self.final_dest = self.enter_final_destination_path.get("1.0", "end-1c")
        self.user_info['final_dest'] = self.final_dest
        if self.save_final_destination_var.get() == True:
            with open('pug_userinfo.txt','w') as fp:
                json.dump(self.user_info, fp)
                self.console.delete('1.0', 'end-1c')
                self.console.insert('1.0', 'Final Destination Has Been Saved and Submitted!')
                self.enter_final_destination_path.configure(bg='#d4d4d4')
        else:
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Final Destination Has Been Submitted!')
        if os.path.exists(self.destination_drive) is False and len(self.destination_drive) > 0:
            os.mkdir(self.destination_drive)
        self.final_dest = self.destination_drive
        
    def populate_final_files(self):
        self.final_files.delete('1.0', "end-1c")
        if os.path.exists(self.final_source) is False:
            self.console.delete('1.0', "end-1c")
            self.console.insert('1.0', "Doesn't look like the Final Source file exists or nothing was entered. Check the Final Source entry!")
        for _,_,f in os.walk(self.final_source):
            if len(f) > 0:
                for files in f:
                    if '.DS' not in files:
                        file = f'{files}\n'
                        self.final_files.insert('1.0', file)
            elif len(f) == 0:
                self.console.delete('1.0', "end-1c")
                self.console.insert('1.0', "Sorry, the Final Source file is not available or nothing was entered!")

    def move_populated_final_files(self):
        s_files = []
        file_move_count = 0 
        for r,_,f in os.walk(self.final_source):
            for files in f:
                if '.DS' not in files:
                    s_files.append(f'{r}/{files}')         
        for r2,_,_ in os.walk(self.final_dest):
            for s_f in s_files:
                files_split = s_f.split('/')[-1]
                print(files_split)
                if os.path.exists(f'{r2}/{files_split}') is False:
                    shutil.copy(s_f,f'{r2}/{files_split}')
                    file_move_count += 1 
        self.final_files.insert('1.0',f'Photos Moved: {file_move_count}\n')

    def show_files(self):
        self.files_to_move.delete('1.0', "end-1c")
        picture_list = []
        hard_drive_list = []
        if os.path.exists(self.source_drive) is True:
            for r, _, f in os.walk(self.source_drive):
                for files in f:
                    if '.NEF' or '.MOV' in files:
                        if '._' and '.xmp' not in files:
                            source_finals = f'{r}/{files}'
                            picture_list.append(source_finals)
        else:
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Sorry, the Source File is not available or nothing was entered!')
        if os.path.exists(self.destination_drive) is True:
            for _, _, f2 in os.walk(self.destination_drive):
                for files2 in f2:
                    hard_drive_list.append(files2)
            for pictures in picture_list:
                if f'{pictures.split("/")[-1]}' not in hard_drive_list:
                    self.files_to_move.insert('1.0', f'\n{pictures}')
                    self.final_picture_list.append(pictures)
        else: 
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Sorry, the Destination File is not available or nothing was entered!')

    def move_files(self):
        num_moved = 0
        if os.path.exists(self.destination_drive) is False:  
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Sorry, the specified destination directory is not available!')
        else:
            if self.dir_name == '':
                self.console.delete('1.0', 'end-1c')
                self.console.insert('1.0', "Enter the destination's directory name below!")  
            else: 
                new_file = self.dir_name
                destination_path = f'{self.destination_drive}/{new_file}'
                if os.path.exists(destination_path) is False:
                    os.mkdir(destination_path)
                for pictures in self.final_picture_list:
                    destination_file = f'{destination_path}/{pictures.split("/")[-1]}'
                    shutil.copy(pictures, f'{destination_file}')
                    self.files_to_move.insert('1.0', f'Moved: {pictures}')
                    num_moved += 1
        self.files_to_move.insert('1.0', f'Photos Moved: {num_moved}\n')

    def dir_name_submit(self):
        if len(self.dest_dir_name.get('1.0',"end-1c")) > 0:
            self.dir_name = self.dest_dir_name.get('1.0',"end-1c")
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Directory Name Has Been Successfully Submitted!')
            self.dest_dir_name.configure(bg='#d4d4d4')
        else:
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Please Enter a Directory Name!')

    def enter_instagramify_root(self):
        self.instagramify_root = self.ig_photo_root.get('1.0',"end-1c")
        self.user_info['instagramify_root'] = self.instagramify_root
        with open('pug_userinfo.txt','w') as fp:
            json.dump(self.user_info, fp)
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', 'Instagramify Root Has Been Saved and Submitted!')
        self.ig_photo_root.configure(bg='#d4d4d4')

    def ig_ify(self):
        if os.path.exists(self.instagramify_root) is True:
            try:
                image_name = self.ig_photo_name.get("1.0", "end-1c")
                im = Image.open(f'{self.final_source}/{image_name}')
                w, h = im.size
                width_ratio = .8 - (w/h)
                new_width = w*(1+width_ratio)
                new_size = round(new_width), round(h)
                background = Image.new('RGB', (new_size), (255, 255, 255, 255))
                background.paste(im, (round((new_width-w)/2), 0))
                background.save(f'{self.instagramify_root}/{image_name.split(".jpg")[0]}_2.jpg')
                self.console.delete('1.0', 'end-1c')
                self.console.insert('1.0', 'Photo has been Instagramified!')
            except IsADirectoryError:
                self.console.delete('1.0', 'end-1c')
                self.console.insert('1.0', "It doesn't look like that photo exists or nothing was entered.")
        else:
            self.console.delete('1.0', 'end-1c')
            self.console.insert('1.0', "It doesn't look like your specified Instagramify Root directory exists.")


def main():
    with open('pug_userinfo.txt', 'r') as fp:
    j = fp.read()
    user_info = json.loads(j)
    root = tk.Tk()
    app = pug_main(root, user_info)
    root.mainloop()

if __name__ == "__main__":
    pass
