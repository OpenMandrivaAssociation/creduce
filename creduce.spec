%define git 20140818

Name: creduce
Version: 2.2.0
Release: %{?git:0.%{git}.}1
%if %{git}
Source0: %{name}-%{git}.tar.xz
%else
Source0: http://embed.cs.utah.edu/creduce/%{name}-%{version}.tar.gz
%endif
# From llvm-svn-compatible branch
Patch0: 0002-update-with-respect-to-clang-s-api-changes.patch
Patch1: 0004-keep-tracking-LLVM-trunk.patch
Patch2: 0008-fixed-one-more-crash.patch
Patch3: 0009-handle-CXXTemporaryObjectExpr.patch
Patch4: 0016-Fixed-an-LLVM-API-breakage.patch
Patch5: 0027-Fixed-an-API-compatibility-issue.patch
# Also needed
Patch6: creduce-compile-with-llvm-3.5.patch
Summary: Tool for creating reduced test cases for compiler bugs
# https://github.com/csmith-project/creduce/tree/llvm-svn-compatible
URL: http://embed.cs.utah.edu/creduce/
License: BSD
Group: Development/Tools
BuildRequires: llvm-devel
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
%setup -qn %{name}
%apply_patches
autoreconf -fi
%configure

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/creduce
