#include "EncrDecr.h"
#include <iostream>

std::string EncrDecr::encrypt(std::string info)
{
    change = "0x";
    // switch them backwards
    // map them to the opposite ends, ASCII 32 - 126
    int j = info.length() + 1;
    for (int i = info.length() - 1; i >= 0; i--)
    {  
        change.push_back(info[i]);
        change[j-i] = 158 - change[j-i];
    }

    info = change.substr(2); 

    //convert to 0 for ASCII !(0-9) and !(B-E)
    //A F
    for (int i = 2; i < change.size(); i++)
    {
        if ((!(change[i] > 47 && change[i] < 58) && !(change[i] > 65 && change [i] < 70)))
        {
            if (change[i] == 'A')
                change[i] = 'F';
            else if (change[i] == 'F')
                change[i] = 'A';
            else
                change[i] = 'A';
        }
        else
        {
            info[i-2] = 'F';
        }
    }
    std::string result = "\"";
    change.append("");
    info.append("\"  ");
    int temp = info.length() + 62;
    info[info.length()-1] = char(temp);
    change.append(info); 
    result.append(change);   
    return result;
}

std::string EncrDecr::decrypt(std::string info, int len)
{
    change = "";
    int jump = len - 65;
    len = len - 63;
    for (int i = 2; i < len; i++)
    {
        if (info[i] == 'A' || info[i] == 'F')
        {
            change.push_back(info[i + jump]);
        }
        else
        {
            change.push_back(info[i]);
        }
    }
    info = change;
    len = jump - 1; 
    for (int i = 0; i < change.length(); i++)
    {
        info[i] = change[len - i];
        info[i] = 158 - info[i];
    }
    return info;
}