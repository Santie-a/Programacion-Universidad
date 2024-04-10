#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

double distancia(double c1[2], double c2[2])
{
    float d = sqrt(pow(c2[0] - c1[0], 2) + pow(c2[1] - c1[1], 2));
    return d;
}

int main()
{
    double c1[2] = {0, 0};
    double c2[2] = {0, 0};

    cout << distancia(c1, c2) << endl;
}