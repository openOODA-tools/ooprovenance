Name:           ooprovenance
Version:        0.1.0
Release:        1%{?dist}
Summary:        Generates SLSA Build Level 3 provenance manifests for all compiled binaries.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooprovenance
Source0:        ooprovenance-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooprovenance is a sovereign, capability-bounded SLSA PROVENANCE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooprovenance
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooprovenance-uninstall

%files
/usr/bin/ooprovenance
/usr/bin/ooprovenance-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
