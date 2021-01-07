%define		plugin		webapi
%define		rev		6f5ffb6
%define		timestamp	20210107
Summary:	Vim plugin: vim interface to Web API
Name:		vim-plugin-%{plugin}
Version:	1.0
Release:	0.%{timestamp}.1
License:	MIT
Group:		Applications/Editors/Vim
Source0:	https://codeload.github.com/mattn/webapi-vim/tar.gz/%{rev}?/%{name}-%{version}-%{rev}.tar.gz
# Source0-md5:	fba9969884454438852d5fa481e8f09f
URL:		https://github.com/mattn/webapi-vim
Requires:	curl
Requires:	vim-rt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
vim interface to Web API with support for following protocols:

 - Basic HTTP
 - OAuth
 - Atompub
 - SOAP (in progress)
 - XMLRPC
 - MetaWeblog API

This library contains:

 - XML Parser
 - HTML Parser(Hack Way)
 - JSON Parser
 - BASE64 Hash Algorithm
 - SHA1 Hash Algorithm
 - HMAC HASH Algorithm
 - Bit Operation Library
 - Converter for "UTF-8 to Unicode"

%package doc
Summary:	Documentation for ebapi Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for webapi Vim plugin.

%prep
%setup -qn webapi-vim-%{rev}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -pr autoload doc $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%doc README.md
%{_vimdatadir}/autoload/webapi

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/webapi*.txt
