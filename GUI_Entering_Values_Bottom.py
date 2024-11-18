import os
import customtkinter as ctk
from PIL import Image
from langchain_community.llms import Ollama
import tkinter as tk
import threading

# Dynamically construct file paths for user and AI images
user_image_path = os.path.join(os.path.expanduser("~"), "Pictures", "Saved Pictures", "user3.png")
ai_image_path = os.path.join(os.path.expanduser("~"), "Pictures", "Saved Pictures", "AI2.png")


# Dynamically construct file paths for Biotechnology and Prototyping logos
Biotechnology_image_path = os.path.join("D:", "Post grad (MSA1)", "Logos", "Biotechnology1.png")
Prototyping_image_path = os.path.join("D:", "Post grad (MSA1)", "Logos", "Prototyping lab.png")

# Verify the paths (optional, to check if the files exist)
for path, label in [
    (user_image_path, "User image"),
    (ai_image_path, "AI image"),
    (Biotechnology_image_path, "Biotechnology logo"),
    (Prototyping_image_path, "Prototyping logo"),
]:
    if not os.path.exists(path):
        print(f"{label} not found at: {path}")
    else:
        print(f"{label} found at: {path}")


# Initialize the selected model
selected_model = "my-analyst"

# Initialize the selected solvent
selected_solvent = "Ethyl acetate"

# Initialize the selected biological agent
selected_biological_agent = "Plant"

# Function to change appearance mode based on selection
def toggle_appearance_mode():
    current_mode = ctk.get_appearance_mode()
    new_mode = "Dark" if current_mode == "Light" else "Light"
    ctk.set_appearance_mode(new_mode)

# Function to handle AI model selection
def select_ai_model(model_choice):
    global selected_model
    selected_model = model_choice

# Function to handle solvent selection
def select_solvent(solvent_choice):
    global selected_solvent
    selected_solvent = solvent_choice

# Function to handle biological agent selection
def select_biological_agent(agent_choice):
    global selected_biological_agent
    selected_biological_agent = agent_choice

# Function to generate the prompt from user inputs
def generate_prompt():
    r = r_entry.get()
    g = g_entry.get()
    b = b_entry.get()
    hex_code = hex_entry.get()
    num = num_entry.get()
    temp = temp_entry.get()
    
    # Retrieve the selected solvent and biological agent
    solvent = selected_solvent
    biological_agent = selected_biological_agent
    
    # Construct the prompt
    prompt = f"Analyze data with the following inputs:\n"
    prompt += f"R: {r}, G: {g}, B: {b}\n"
    prompt += f"Hex: {hex_code}\n"
    prompt += f"Numerical Value: {num}\n"
    prompt += f"Temperature: {temp}\n"
    prompt += f"Solvent: {solvent}\n"
    prompt += f"Biological Agent: {biological_agent}\n"
    
    return prompt

def analyze_data(prompt):
    # Display a loading indicator
    loading_label.pack(pady=5)

    try:
        # Perform AI-based data analysis using the selected model and get the response
        llm = Ollama(model=selected_model)
        response = llm.invoke(prompt)
        print(f"AI Response: {response}")  # Print the response for debugging
    except Exception as e:
        print(f"Error: {e}")  # Print any exceptions for debugging
        response = "An error occurred while processing your request."

    # Remove the loading indicator
    loading_label.pack_forget()

    # Display the response in the chat history
    display_message("AI", response, "#32a852", "w")

# Function to display a message in the chat history
def display_message(sender, message, color, side):
    # Create a frame for the entire message (image + text)
    message_container = ctk.CTkFrame(chat_scrollable_frame, fg_color="transparent")
    message_container.pack(pady=5, padx=10, anchor=side)

    if sender == "User":
        image_path = user_image_path
        anchor_side = "e"
        msg_side = "left"
        img_side = "right"
        msg_bg = "#32a852"  # Customize user message background color if needed
    else:
        image_path = ai_image_path
        anchor_side = "w"
        msg_side = "right"
        img_side = "left"
        msg_bg = "#6699CC"  # Customize AI message background color if needed

    # Resize the image
    try:
        original_image = Image.open(image_path)
        image = ctk.CTkImage(original_image, size=(35, 35))
        image_label = ctk.CTkLabel(message_container, image=image, text="")
        image_label.pack(side=img_side, padx=5)
    except FileNotFoundError:
        print(f"File not found: {image_path}")

    # Create the message bubble frame and pack it
    message_frame = ctk.CTkFrame(message_container, fg_color=msg_bg)
    message_frame.pack(side=msg_side, fill="x", expand=True, padx=5)

    # Create the message label and pack it
    message_label = ctk.CTkLabel(message_frame, text=message, font=("Raleway", 14), wraplength=1000, justify="left", fg_color=msg_bg)
    message_label.pack(padx=10, pady=5)

# Function to handle the send button click
def send_message(event=None):
    prompt = generate_prompt()
    if prompt.strip():
        display_message("User", prompt, "#6699CC", "e")  # Display the user's message immediately
        clear_entries()  # Clear the entry fields
        threading.Thread(target=analyze_data, args=(prompt,)).start()  # Start a new thread for analyze_data

# Function to clear entry fields
def clear_entries():
    r_entry.delete(0, tk.END)
    g_entry.delete(0, tk.END)
    b_entry.delete(0, tk.END)
    hex_entry.delete(0, tk.END)
    num_entry.delete(0, tk.END)
    temp_entry.delete(0, tk.END)

# Separate the GUI logic
def create_gui():
    global window, prompt_entry, chat_frame, loading_label, chat_scrollable_frame
    global r_entry, g_entry, b_entry, hex_entry, num_entry, temp_entry

    # Create the main window
    window = ctk.CTk()
    window.title("AI based data analysis application")
    window.geometry("800x600")

    # Set the default appearance mode to dark
    ctk.set_appearance_mode("Dark")

    # Create a frame for the images, title, appearance mode, model selection, solvent selection, and biological agent selection
    # Create a frame for the images and title
    image_title_frame = ctk.CTkFrame(window)
    image_title_frame.pack(side="top", padx=10, pady=10, fill="x")

    # Load and resize the left image
    left_image_path = Prototyping_image_path
    left_original_image = Image.open(left_image_path)
    left_my_image = ctk.CTkImage(left_original_image, size=(90, 90))

    # Use image_title_frame as the parent widget for CTkLabel
    left_image_label = ctk.CTkLabel(image_title_frame, image=left_my_image, text="")
    left_image_label.pack(side="left", padx=10)  # Display the label on the left

    # Create a label for the title
    title_label = ctk.CTkLabel(image_title_frame, text="AI based data analysis application", font=("Montserrat", 20, "bold"))
    title_label.pack(side="left", expand=True, padx=10)  # Center the title

    # Load and resize the right image
    right_image_path = Biotechnology_image_path
    right_original_image = Image.open(right_image_path)
    right_my_image = ctk.CTkImage(right_original_image, size=(100, 100))

    # Use image_title_frame as the parent widget for CTkLabel
    right_image_label = ctk.CTkLabel(image_title_frame, image=right_my_image, text="")
    right_image_label.pack(side="right", padx=10)  # Display the label on the right

    # Create the chat frame
    chat_frame = ctk.CTkFrame(window)
    chat_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Create the scrollable frame for chat history
    chat_scrollable_frame = ctk.CTkScrollableFrame(chat_frame, width=780, height=400)
    chat_scrollable_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Create a frame for the appearance mode, model selection, solvent selection, and biological agent selection
    selection_frame = ctk.CTkFrame(window)
    selection_frame.pack(side="top", padx=10, pady=10)

    # Create the appearance mode toggle switch
    appearance_mode_switch = ctk.CTkSwitch(window, text="", command=toggle_appearance_mode)
    appearance_mode_switch.place(x=1320, y=109)
    
    # Create a frame for the AI model selection
    model_frame = ctk.CTkFrame(selection_frame)
    model_frame.pack(side="left", padx=10)

    # Create a label for the AI model selection
    model_label = ctk.CTkLabel(model_frame, text="AI Model", font=("Raleway", 14, "bold"))
    model_label.pack(side="left", padx=10)

    # Create the AI model option menu
    model_optionmenu = ctk.CTkOptionMenu(model_frame, values=["llama3", "phi3", "my-analyst"], command=select_ai_model, font=("Raleway", 12))
    model_optionmenu.pack(side="left", padx=10)
    model_optionmenu.set("my-analyst")  # Default to "phi3" model

    # Create a frame for the solvent selection
    solvent_frame = ctk.CTkFrame(selection_frame)
    solvent_frame.pack(side="left", padx=10)

    # Create a label for the solvent selection
    solvent_label = ctk.CTkLabel(solvent_frame, text="Extracting Solvent", font=("Raleway", 14, "bold"))
    solvent_label.pack(side="left", padx=10)

    # Create the solvent option menu
    solvent_optionmenu = ctk.CTkOptionMenu(solvent_frame, values=["Ethyl acetate", "Methanol", "Hexane", "Chloroform"], command=select_solvent, font=("Raleway", 12))
    solvent_optionmenu.pack(side="left", padx=10)
    solvent_optionmenu.set("Ethyl acetate")  # Default to "Ethyl acetate")

    # Create a frame for the biological agent selection
    agent_frame = ctk.CTkFrame(selection_frame)
    agent_frame.pack(side="left", padx=10)

    # Create a label for the biological agent selection
    agent_label = ctk.CTkLabel(agent_frame, text="Biological Agent", font=("Raleway", 14, "bold"))
    agent_label.pack(side="left", padx=10)

    # Create the biological agent option menu
    agent_optionmenu = ctk.CTkOptionMenu(agent_frame, values=["Plant", "Bacteria", "Fungi"], command=select_biological_agent, font=("Raleway", 12))
    agent_optionmenu.pack(side="left", padx=10)
    agent_optionmenu.set("Plant")  # Default to "Plant"

    # Create the frame for data inputs
    data_entry_frame = ctk.CTkFrame(window)
    data_entry_frame.pack(padx=10, pady=10)
    
    # Create the entry fields for R, G, B values, Hex code value, Numerical value, and Temperature value
    r_label = ctk.CTkLabel(data_entry_frame, text="R:", font=("Raleway", 14, "bold"))
    r_label.pack(side="left", padx=10)
    r_entry = ctk.CTkEntry(data_entry_frame)
    r_entry.pack(side="left", padx=10)

    g_label = ctk.CTkLabel(data_entry_frame, text="G:", font=("Raleway", 14, "bold"))
    g_label.pack(side="left", padx=10)
    g_entry = ctk.CTkEntry(data_entry_frame)
    g_entry.pack(side="left", padx=10)

    b_label = ctk.CTkLabel(data_entry_frame, text="B:", font=("Raleway", 14, "bold"))
    b_label.pack(side="left", padx=10)
    b_entry = ctk.CTkEntry(data_entry_frame)
    b_entry.pack(side="left", padx=10)

    hex_label = ctk.CTkLabel(data_entry_frame, text="Hex:", font=("Raleway", 14, "bold"))
    hex_label.pack(side="left", padx=10)
    hex_entry = ctk.CTkEntry(data_entry_frame)
    hex_entry.pack(side="left", padx=10)

    num_label = ctk.CTkLabel(data_entry_frame, text="Numerical:", font=("Raleway", 14, "bold"))
    num_label.pack(side="left", padx=10)
    num_entry = ctk.CTkEntry(data_entry_frame)
    num_entry.pack(side="left", padx=10)

    temp_label = ctk.CTkLabel(data_entry_frame, text="Temperature:", font=("Raleway", 14, "bold"))
    temp_label.pack(side="left", padx=10)
    temp_entry = ctk.CTkEntry(data_entry_frame)
    temp_entry.pack(side="left", padx=10)

    # Create the frame for the send button and input prompt
    send_frame = ctk.CTkFrame(window)
    send_frame.pack(padx=10, pady=10)

    # Create a button to send the prompt for analysis
    send_button = ctk.CTkButton(send_frame, text="Analyze", command=send_message, font=("Raleway", 14, "bold"))
    send_button.pack(side="left", padx=10)

    #Create the loading label
    loading_label = ctk.CTkLabel(send_frame, text="Loading...", font=("Raleway", 14, "bold"))

    # Bind the Enter key to the send_message function
    window.bind("<Return>", send_message)
    
    # Start the main event loop
    window.mainloop()

# Run the GUI application
create_gui()
