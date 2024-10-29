#include<iostream>
#include<vector>
#include<ctime>
#include<string>


using namespace std;

string randprogression(string notes[], vector<string> quality, int n);

int main()
{   
    srand(time(NULL));
    string notes[12] = {"C","Db","D","Eb","E","F","Gb","G","Ab","A",
    "Bb","B"};

    vector<string> quality = {"maj","min","sus2","sus4","majb5","dim",
    "maj7","min7","7","maj7#11","min6","7#11","maj7#5","maj69",
    "dimmaj7","min7b5"};

    cout << randprogression( notes,quality, 4) << endl;
    cout <<"Pozycja: "<< rand()%4 + 1 <<endl;
    //1 pozycja od 1 progu
    //2 pozycja od 5 progu
    //3 pozycja od 10 progu
    //4 pozycja od 15 progu



    return 0;
}




string randprogression(string notes[], vector<string> quality, int n)
{
    string prog = "";
    string randnote;
    string randquality;
    for(int i = 0; i < n; i++)
    {
        randnote = notes[rand()%12];
        randquality = quality[rand()%quality.size()];
        
        prog += randnote + randquality + " ";
    }
    return prog;
}