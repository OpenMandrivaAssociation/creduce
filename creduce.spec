%define git 20210819

Name: creduce
Version: 2.11.0
%if 0%{git}
Release: 0.%{git}.1
Source0: https://github.com/csmith-project/creduce/archive/master/%{name}-%{git}.tar.gz
%else
Release: 1
Source0: http://embed.cs.utah.edu/creduce/%{name}-%{version}.tar.gz
%endif
# From upstream llvm-12.0-dev branch
Patch0: https://github.com/csmith-project/creduce/commit/3e1f5a1ec1365fafae965c97603221c9ccbc2d61.patch
Patch1: https://github.com/csmith-project/creduce/commit/d45d5455558bacca3e5d6c3fffb3992b78f432aa.patch
Patch2: https://github.com/csmith-project/creduce/commit/5e00bcfd691a3dde5c89c00d402b14bbeb13b6de.patch
# Make it work
Patch4: creduce-llvm-12.patch
# And port to llvm-13
Patch5: creduce-llvm-13.patch
Summary: Tool for creating reduced test cases for compiler bugs
# https://github.com/csmith-project/creduce
URL: http://embed.cs.utah.edu/creduce/
License: BSD
Group: Development/Tools
BuildRequires: llvm-devel
BuildRequires: clang-devel
BuildRequires: llvm-polly-devel
BuildRequires: flex
BuildRequires: perl(File::Which)
BuildRequires: perl(Getopt::Tabular)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Term::ReadKey)
Requires: clang
Requires: flex
Requires: astyle
Requires: indent
Requires: delta

%description
C-Reduce is a tool that takes a large C or C++ program that has a
property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ program that has the
same property. It is intended for use by people who discover and
report bugs in compilers and other tools that process C/C++ code.

%prep
%if 0%{git}
%autosetup -p1 -n %{name}-master
%else
%autosetup -p1 -n %{name}-%{version}
%endif

%build
CXXFLAGS="%{optflags} -std=gnu++1y -D__STDC_LIMIT_MACROS=1 -D__STDC_CONSTANT_MACROS=1" %configure

%make_build

%install
%make_install

%files
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/creduce
