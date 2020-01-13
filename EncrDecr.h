# ifndef EncrDecr_H
# define EncrDecr_H
#include <string>

class EncrDecr
{
public:
    std::string encrypt(std::string password);
    std::string decrypt(std::string password, int len);

private:
    std::string change;
};

# endif