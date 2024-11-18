# **<p align="center"> Customized-AI-Data-Analysis-App </p>**
## <p align="center"> A customized AI-based data analysis app for the DIY smart crude extractor </p>
## <p align="center"> RDI Prototyping Lab, Faculty of Biotechnology, MSA university </p>
<p align="center"> Authors: Doha Ibrahim, Salma Abdelrahem, Mohamed Tarek, and Ahmed Gomaa. </p>
 
<p align="center"> 
<img src= "6-pbr.png"> 
</p>

Welcome to the Customized AI Data Analysis App for the DIY Smart Crude Extractor!
This Python-based application uses AI to analyze data from a smart crude extractor and predict the composition of crude mixtures in extracting solvents. By inputting data such as RGB values, Hex codes, temperature, solvent type, and biological agent, the system leverages advanced Ollama AI models, including Llama 3, Phi 3, and a customized Phi 3 model named My-Analyst. the system processes these data points to predict the likely composition of the mixture. It identifies bioactive compounds such as pigments, flavonoids, and phenolic substances based on the sensor readings, enhancing the analysis and optimization of bioactive compound extraction. 

## Features

### 1. **AI-Powered Data Analysis:**
Leverages advanced Ollama AI models, including Llama 3, Phi 3, and the customized Phi 3 model (My-Analyst), to analyze and predict the composition of crude mixtures.

### 2. **Real-Time Extraction Monitoring & Optimization:**
Processes data inputs in real-time, providing immediate predictions of bioactive compounds. Offers insights into compound stability and solvent efficiency for optimized extraction processes.

### 3. **Bioactive Compound Prediction:**
Identifies potential bioactive compounds such as pigments, flavonoids, phenolic substances, and more, based on sensor data.

### 4. **User-Friendly & DIY-Ready:**
Simple interface with a chat-like display for AI responses. Easily input data to receive precise predictions, enhancing usability for researchers and developers.

### 5. **Customizable & Extendable:**
Open to modifications, allowing integration of additional sensors, AI models, or specific compound databases to extend functionality.

## Installation

1. **Clone the repository**:
   - First, clone the project repository to your local machine using the following command:
     ```bash
     git clone https://github.com/Doha-Ibrahim/Customized-AI-Data-Analysis-App.git
     ```

### Instructions for Users

1. **Install Ollama**:  
   - Go to the [Ollama download page](https://ollama.com/download), download the appropriate version for your operating system, and follow the installation steps.
   
2. **Install Required Libraries**:  
   - After installing Ollama, open a terminal (command prompt, PowerShell, or terminal on Linux/macOS) and run:
     ```bash
     pip install ollama
     ```

3. **Run Pre-Trained Models**:  
   - Use the following commands to run **Llama3** or **Phi3 Mini**:
     ```bash
     ollama run llama3
     ```
     and
     ```bash
     ollama run phi3
     ```

4. **Run Customized AI Model (`my-analyst`)**:
   - First, create the custom model by running:
     ```bash
     ollama create my-analyst -f My-model.md
     ```
   - Then, run the model with:
     ```bash
     ollama run my-analyst
     ```
   - Finally, start the server for real-time AI interaction:
     ```bash
     ollama serve
     ```
## Running the application

 1. **Navigate to the Project Directory**:
    - After cloning the repository, change into the project directory by running:
      ```bash
      cd Customized-AI-Data-Analysis-App
      ```
2. **Run the Application**:
    - Once all previous steps are complete, you can now run the project. In the project directory, execute one of the following command to start the application:
      
      ```bash
      python run_project.py
      ```
      or
      ```bash
      python src/main_code_v2.py
      ```
      or
      ```bash
      python src/main_code_v3.py
      ```
    - This will start the application, and you will be able to interact with the customized AI model and perform data analysis tasks.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution and Collaboration:

We invite the community to contribute to the development of this customized AI-based data analysis app for the smart crude extractor. Whether you're skilled in data analysis, machine learning, or sensor technologies, your contributions are invaluable. Feel free to submit issues, pull requests, track bugs, or join discussions to help improve the prediction models and enhance the overall system. Together, we can enhance the system’s ability to analyze extraction data and predict bioactive compounds more accurately.

## Acknowledgments

We gratefully acknowledge the open-source communities whose tools and resources supported the development of this project.

## Contributors
Doha Ibrahim, 
Salma Abdelrahem, and
Mohamed Tarek.
Supervised by: Dr. Ahmed Gomaa.
