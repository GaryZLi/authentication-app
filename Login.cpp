#include <iostream>
#include <string>
#include "EncrDecr.h"

int main(int argc, char** argv)
{	
	// argv[0] = cmd, argv[1] = username, argv[3] = pass
	if (argc == 3)
	{
		std::string getUser, getPass;
		getUser = argv[1];
		getUser = getUser.substr(1, getUser.length()-2);
		getPass = argv[2];
		getPass = getPass.substr(1, getPass.length()-2);

		EncrDecr info;
		// std::string retUser, retPass;// = "\"";
		// retUser.append(info.encrypt(getUser));
		// retUser.append("\"");
		// retPass.append(info.encrypt(getPass));
		// retUser.append("\"");
		std::cout << info.encrypt(getUser) << " " << info.encrypt(getPass);// << retPass;
	}
	// argv[0] = cmd, argv[1] = username, argv[2] = username length, argv[3] = pass, argv[4] = pass length
	else
	{
		// for (int i = 0; i < argc; i++)
		// 	std::cout << argv[i] << std::endl;
		std::string getUser, getPass;
		getUser = argv[1];
		getUser = getUser.substr(1, getUser.length()-2);
		getPass = argv[3];
		getPass = getPass.substr(1, getPass.length()-2);

		char userLen = *argv[2];
		char passLen = *argv[4];

		EncrDecr info;
		std::cout << info.decrypt(getUser, userLen) << " " << info.decrypt(getPass, passLen);
	}

	return 0;
}