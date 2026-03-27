#include "common.h" 

int main(int argc, char *argv[]){ 
    // OS gives the input fot these argumnets
    // argc -> number of parameters passed
    // argv -> array of parameters

    if(argc < 2){    // Here 2 because the length of the array argv is 2 i.e) Two argumnets are passed as an array in subprocess
        printf("Invalid Input\n");
        return 1;
    }

    struct Patient p;

    char data[750];
    strcpy(data, argv[1]);

    char *token;

    //Parse data
    token = strtok(data, "|");
    strcpy(p.name, token);

    token = strtok(NULL, "|");
    p.age = atoi(token);

    token = strtok(NULL, "|");
    strcpy(p.gender, token);

    token = strtok(NULL, "|");
    strcpy(p.phone, token);

    token = strtok(NULL, "|");
    strcpy(p.address, token);

    token = strtok(NULL, "|");
    strcpy(p.symptoms, token);

    token = strtok(NULL, "|");
    strcpy(p.visit_type, token);

    token = strtok(NULL, "|");
    strcpy(p.priority, token);

    // Reading and Writing data in file

    FILE* fp;
    int count = 0;
    char line[1024];

    fp = fopen("Backend/patients.txt", "r");

    if(fp != NULL){
        while(fgets(line, sizeof(line), fp)){
                count++;
            }
        fclose(fp);
    }

    p.id = count + 1;

    fp = fopen("Backend/patients.txt", "a");

    fprintf(fp, "%d|%s|%d|%s|%s|%s|%s|%s|%s\n",
            p.id, p.name, p.age, p.gender, p.phone,
            p.address, p.symptoms, p.visit_type, p.priority);

    fclose(fp);
    

    // This is the Output that will be displayed in the page
    printf("%d|%s|%s", p.id, p.visit_type, p.priority);

    return 0;
}