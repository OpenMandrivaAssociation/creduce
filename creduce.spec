%define git %nil

Name: creduce
Version: 2.8.0
%if 0%{git}
Release: 0.%{git}.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 3
Source0: http://embed.cs.utah.edu/creduce/%{name}-%{version}.tar.gz
%endif
Summary: Tool for creating reduced test cases for compiler bugs
# https://github.com/csmith-project/creduce
URL: http://embed.cs.utah.edu/creduce/
License: BSD
Group: Development/Tools
BuildRequires: llvm-devel
BuildRequires: clang-devel
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
# From llvm-svn-compatible branch
Patch100:	0001-Fixes-140-Support-version-flag.patch
Patch101:	0002-Increment-version-number-to-2.9.0.patch
Patch102:	0003-Fix-option-name.patch
Patch103:	0004-Handle-DependentScopeDeclRefExpr.patch
Patch104:	0005-Iterate-a-CXXRecordDecl-only-if-it-has-definition.patch
Patch105:	0006-Check-number-of-CPUs-only-if-n-wasn-t-specified.patch
Patch106:	0007-Fix-typo.patch
Patch107:	0008-Handle-non-constant-array-types.patch
Patch108:	0009-Fixed-an-issue-for-rewriting-record-decls.patch
Patch109:	0010-Allow-tests-with-.cc-postfix.patch
Patch110:	0011-Added-a-new-test.patch
Patch111:	0012-Fixed-issues-for-empty-struct-to-int.patch
Patch112:	0013-avoid-overwritting-destructors-when-renaming-classes.patch
Patch113:	0014-Fixed-an-issue-for-empty-struct-to-int.patch
Patch114:	0015-Use-a-different-name-for-the-sub-loop.patch
Patch115:	0016-make-InclusionDirective-virtual.patch
Patch116:	0017-Fixed-a-Wreturn-type-warning.patch
Patch117:	0018-Fixed-a-crash-for-removing-explicit-instantiation.patch
Patch118:	0019-avoid-removing-nested-calls-from-member-initializers.patch
Patch119:	0020-Update-RemoveUnusedEnumMember.h.patch
Patch120:	0021-Update-include-guard.patch
Patch121:	0022-take-syntactic-form-only-if-it-s-non-null.patch
Patch122:	0023-built-with-LLVM-7.0.patch
Patch123:	0024-change-ordering-so-pass_includes-is-called-after-pas.patch
Patch124:	0025-add-pass-to-remove-constant-ifs.patch
Patch125:	0026-add-pass-for-line-markers.patch
Patch126:	0027-add-binary-search-removal-of-c-style-comments.patch
Patch127:	0028-convert-to-markdown.patch
Patch128:	0029-patch-from-Mingwandroid-to-update-to-LLVM-7.patch
Patch129:	0030-skip-inlining-calls-in-default-arguments.patch
Patch130:	0031-Update-llvm-svn-compatible-branch-for-ToT-clang.patch

%description
C-Reduce is a tool that takes a large C or C++ program that has a
property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ program that has the
same property. It is intended for use by people who discover and
report bugs in compilers and other tools that process C/C++ code.

%prep
%if 0%{git}
%autosetup -p1 -n %{name}-%{name}-%{version}
%else
%autosetup -p1 -n %{name}-%{name}-%{version}
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
