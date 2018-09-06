%define git %nil

Name: creduce
Version: 2.8.0
%if 0%{git}
Release: 0.%{git}.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: http://embed.cs.utah.edu/creduce/%{name}-%{version}.tar.gz
%endif
Summary: Tool for creating reduced test cases for compiler bugs
# https://github.com/csmith-project/creduce
URL: http://embed.cs.utah.edu/creduce/
License: BSD
Group: Development/Tools
BuildRequires: llvm-devel clang-devel
BuildRequires: flex
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
%setup -qn %{name}-%{name}-%{version}
%else
%setup -qn %{name}-%{name}-%{version}
%endif
%apply_patches

%build
autoreconf -fi
CXXFLAGS="%{optflags} -std=gnu++1y -D__STDC_LIMIT_MACROS=1 -D__STDC_CONSTANT_MACROS=1" %configure

%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/creduce
